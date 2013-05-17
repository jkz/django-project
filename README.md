Django Project
==============

A Django project template

Project expects a top-level directory named 'local'. This folder and its
structure is created by 'bootstrap.py', either within the project by
default, or symlinking a given location.


Installation
============

Run the portable bootstrap script:

    ./bootstrap.py

Add shared python and django packages and modules:

    cd local/share
    ln -s ~/django/share django
    ln -s ~/python/share python

Currently, there are some dependencies resolved by this. In future, when
the apps are more fleshed out, they'll be included in requirements.pip
