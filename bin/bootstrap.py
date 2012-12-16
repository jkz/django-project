#!/usr/bin/env python

import os
import sys
import subprocess

#TODO: make a setenv manage command

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
NAME = os.path.split(ROOT)[1]
LOCAL = os.path.join(ROOT, 'local')

def try_mkdir(path):
    try:
        os.makedirs(path)
    except OSError:
        pass

def main():
    try:
        env = sys.argv[1]
    except IndexError:
        exit("Usage: python bootstrap.py <stage>")

    print 'cd %s' % ROOT
    os.chdir(ROOT)
    print 'mkdir local'
    try_mkdir(LOCAL)

    print 'cd local'
    os.chdir(LOCAL)
    print 'mkdir log'
    try_mkdir('log')
    print 'mkdir -p cache/egg'
    try_mkdir('cache/egg')
    print 'mkdir shared_env'
    try_mkdir('shared_env')
    print 'mkdir celery'
    try_mkdir('celery')

    # Create the virtualenv with virtualenvwrapper
    envname = '%s@%s' % (env, NAME)
    envdir = os.path.join(LOCAL, envname)

    print 'virtualenv', envdir
    subprocess.call(['virtualenv', envdir])

    venvrc = os.path.join(LOCAL, 'venvrc.sh')
    if not os.path.exists(venvrc):
        subprocess.call(['touch', venvrc])

    pathcommand = '\n# Put your startup script in here\nsource %s' % venvrc
    envactivate = os.path.join(envdir, 'bin', 'activate')
    with open(envactivate, 'a') as f:
        f.write(pathcommand)

    try:
        print 'ln -s %s venv' % os.path.join(envdir)
        os.symlink(envdir, 'venv')
    except OSError:
        pass


    with open('ENV', 'w') as f:
        f.write(env)

    print 'cd ..'
    os.chdir(ROOT)

    print 'pip install -r requirements.pip', envdir
    subprocess.call(['pip', 'install', '-r', os.path.join([ROOT.encode(), 'requirements.pip'])])


if __name__ == '__main__':
    main()
