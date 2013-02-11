#!/usr/bin/env python
import os, sys


if __name__ == "__main__":
    import site
    ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    SOURCE = os.path.join(ROOT, 'src')
    LOCAL = os.path.join(ROOT, 'local')
    SHARE = os.path.join(LOCAL, 'share')
    SITE_PACKAGES = os.path.join(LOCAL, 'venv', 'lib', 'python2.7', 'site-packages')

    site.addsitedir(SITE_PACKAGES)
    site.addsitedir(SOURCE)
    site.addsitedir(SHARE)

    for path in os.listdir(SHARE):
        PATH = os.path.join(SHARE, path)
        if os.path.isdir(PATH):
            site.addsitedir(PATH)


    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
