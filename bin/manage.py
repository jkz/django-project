#!/usr/bin/env python

if __name__ == "__main__":
    from . import setup_environment
    setup_environment()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
