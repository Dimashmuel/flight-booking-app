#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""

import os
import sys

def main():
    """
    Main entry point for Django's command-line utility.
    - Sets the default settings module for Django.
    - Attempts to execute command-line instructions (e.g., runserver, migrate).
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_project.settings')

    try:
        # Import the command-line executor from Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an error if Django isn't installed or can't be imported
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Run the command passed via CLI
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
