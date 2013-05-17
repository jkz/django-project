#!/usr/bin/env python

import os
import sys
import subprocess

ROOT = os.path.dirname(os.path.realpath(__file__))

def try_mkdir(path, *args):
    try:
        os.makedirs(path, *args)
    except OSError:
        pass

def main():
    try:
        LOCAL = os.path.realpath(sys.argv[1])
    except IndexError:
        LOCAL = os.path.join(ROOT, 'local')

    #TODO: make this an argument
    env = 'dev'

    print('cd {}'.format(ROOT))
    os.chdir(ROOT)
    print('mkdir local')
    try_mkdir(LOCAL)
    print('cd local')
    os.chdir(LOCAL)
    print('mkdir data')
    try_mkdir('data', 0777)
    print('mkdir log')
    try_mkdir('log')
    print('mkdir -p cache/egg')
    try_mkdir('cache/egg')
    print('mkdir share')
    try_mkdir('share')

    # Create the virtualenv with virtualenvwrapper
    ENV = os.path.join(LOCAL, 'venv')

    print('virtualenv', ENV)
    subprocess.call(['virtualenv', ENV])

    activate = os.path.join(ENV, 'bin', 'activate')
    print('source', activate)
    subprocess.call(['source', activate], shell=True)

    print('cd ..')
    os.chdir(ROOT)

    print('pip install -r requirements.pip')
    pip = os.path.join(ENV, 'bin', 'pip')
    subprocess.call([pip, 'install', '-r', os.path.join(ROOT.encode(), 'requirements.pip')])


    settings_path = os.path.join('src', 'conf', 'settings')
    print('cd', settings_path)
    os.chdir(settings_path)

    settings_template = 'local.py.{}'.format(env)
    print('cp', settings_template, 'local.py')
    subprocess.call(['cp', settings_template, 'local.py'])


if __name__ == '__main__':
    main()
