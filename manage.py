#!/usr/bin/env python
import os
import sys

from os import getenv
from dotenv import load_dotenv


if __name__ == "__main__":
    """Run administrative tasks."""
    load_dotenv()

    django_settings_module = getenv('DJANGO_SETTINGS_MODULE', 'app.settings.development')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
execute_from_command_line(sys.argv)
