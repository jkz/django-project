#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import argparse

ROOT = os.path.dirname(os.path.realpath(__file__))

def try_mkdir(path, *args):
    try:
        os.makedirs(path, *args)
    except OSError:
        pass

# http://patorjk.com/software/taag/#p=display&h=2&f=Slant
BANNERS = {
    'project': (
        "    ____               _           __ ",
        "   / __ \_________    (_)__  _____/ /_",
        "  / /_/ / ___/ __ \  / / _ \/ ___/ __/",
        " / ____/ /  / /_/ / / /  __/ /__/ /_  ",
        "/_/   /_/   \____/_/ /\___/\___/\__/  ",
        "                /___/                 "),
    'dev': (
        "         __         ",
        "    ____/ /__ _   __",
        "   / __  / _ \ | / /",
        " _/ /_/ /  __/ |/ / ",
        "(_)__,_/\___/|___/  "),
    'test': (
        "     __            __ "
        "    / /____  _____/ /_"
        "   / __/ _ \/ ___/ __/"
        " _/ /_/  __(__  ) /_  "
        "(_)__/\___/____/\__/  "),
    'prod': (
        "                           __",
        "     ____  _________  ____/ /",
        "    / __ \/ ___/ __ \/ __  / ",
        " _ / /_/ / /  / /_/ / /_/ /  ",
        "(_) .___/_/   \____/\__,_/   ",
        " /_/                         "),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default='dev',
            choices=['dev', 'test', 'prod'], help="set deploy environment")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity",
            action="store_true")
    parser.add_argument("-l", "--local", help="set local directory location")
    args = parser.parse_args()
    if args.local:
        LOCAL = os.path.realpath(args.local)
    else:
        LOCAL = os.path.join(ROOT, 'local')

    env = getattr(args, 'env', 'dev')
    for line in zip(BANNERS['project'], BANNERS[env]):
        print(line[0]+line[1])

    os.chdir(ROOT)
    try_mkdir(LOCAL)
    os.chdir(LOCAL)
    try_mkdir('data')
    try_mkdir('log')
    try_mkdir('cache/egg')
    try_mkdir('share')

    print("""
        Create directory tree

        local
        ├── cache
        │   └── egg
        ├── data
        ├── log
        ├── share
        └── venv
        """)


    # Create the virtualenv with virtualenvwrapper
    ENV = os.path.join(LOCAL, 'venv')

    python = os.path.normpath(sys.executable)
    print("Setup your virtual environment")
    print('virtualenv', '-p', python, ENV)

    if subprocess.call(['virtualenv', '-p', python, ENV]):
        raise Exception("virtualenv failed")

    print()

    site_packages = os.path.join(ENV, 'lib',
            'python{}.{}'.format(*sys.version_info[:2]), 'site-packages')
    print('symlink', site_packages)
    site_packages_link = os.path.join(LOCAL, 'share', 'site-packages')
    if not os.path.lexists(site_packages_link):
        print('ln -s', site_packages, 'local/share')
        os.symlink(site_packages, site_packages_link)

    print('cd ..')
    os.chdir(ROOT)

    req = '-r requirements/{}.pip'.format(env)
    print("echo '{}' > 'requirements.txt".format(req))
    with open('requirements.txt', 'w') as handle:
        handle.write(req)

    print('pip install -r requirements.txt')
    p = subprocess.call([
        os.path.join(ENV, 'bin', 'pip'), 'install',
        '--log', os.path.join(LOCAL, 'log', 'bootstrap.log'),
        '--verbose',
        #'--environment', ENV,
        '-r', os.path.join(ROOT, 'requirements.txt'),
    ])

    settings_path = os.path.join('src', 'conf', 'settings')
    print('cd', settings_path)
    os.chdir(settings_path)

    settings_template = 'local.py.{}'.format(env)
    print()
    print("Copying local settings from {} template".format(env))
    print('cp', settings_template, 'local.py')
    subprocess.call(['cp', settings_template, 'local.py'])


if __name__ == '__main__':
    main()
