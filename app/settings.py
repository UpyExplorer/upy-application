import os

DJANGO_ENV = os.environ.get('DJANGO_ENV')

from .conf.production.settings import *
