#!/usr/bin/env python
# coding=utf-8
# stdlib
import os
import sys
from pathlib import Path

# django
import environ

PROJECT_DIR = Path(__file__).resolve().parent
env = environ.Env()
env.read_env(env_file=str(PROJECT_DIR / ".env"))


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", env("SETTINGS_MODULE"))
    try:
        # django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
