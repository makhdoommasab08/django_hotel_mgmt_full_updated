#!/usr/bin/env python
import os, sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotelmgmt.settings')
    try:
        from importlib import import_module
        execute_from_command_line = import_module('django.core.management').execute_from_command_line
    except Exception as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH? "
            "Activate a virtual environment or install Django with 'pip install django'."
        ) from exc
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    main()
