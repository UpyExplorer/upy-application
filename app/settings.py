import os

DJANGO_ENV = os.environ.get('DJANGO_ENV')

if DJANGO_ENV == 'production':
    from .conf.production.settings import *
else:
    from .conf.development.settings import *