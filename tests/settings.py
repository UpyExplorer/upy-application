import os
from os.path import dirname

BASE_DIR = dirname(dirname(os.path.abspath(__file__)))

EMAIL_HOST_USER = "email@upy.com"
DEFAULT_FROM_EMAIL = "email@upy.com"
SECRET_KEY = "key"
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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
    'modules.ads',
    'modules.seller',
    'modules.customer',

    # Forms
    'widget_tweaks',
    'crispy_forms',
	'bootstrap_modal_forms',

    # Permissions
    'global_permissions',

    # Logs
    'models_logging',
]