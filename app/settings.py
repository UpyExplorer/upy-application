import os
import environ
from os.path import dirname

BASE_DIR = dirname(dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env(BASE_DIR+"/.env")

DJANGO_ENV = env("DJANGO_ENV")

if DJANGO_ENV == 'production':
    from .conf.production.settings import *
else:
    from .conf.development.settings import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'whitenoise.runserver_nostatic',
    'pipeline',

    # Vendor apps
    'bootstrap5',

    # Application apps
    'modules.base',
    'modules.log',
    'modules.api',
    'modules.account',
    'modules.dashboard',
    'modules.company',
    'modules.sale',
    'modules.catalog',
    'modules.application',
    'modules.advertising',

    # Forms
    'widget_tweaks',
    'crispy_forms',
	'bootstrap_modal_forms',

    # Permissions
    'global_permissions',

    # Logs
    'models_logging',
]
