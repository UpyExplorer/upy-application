import os
import warnings

from os.path import dirname
from django.utils.translation import gettext_lazy as _
warnings.simplefilter('error', DeprecationWarning)

BASE_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "KEY")

DEBUG = True
ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

SITE_ID = 1

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
    'bootstrap5',
    'modules.base',
    'modules.log',
    'modules.account',
    'modules.dashboard',
    'modules.company',
    'modules.sale',
    'modules.catalog',
    'modules.application',
    'modules.ads',
    'modules.seller',
    'modules.customer',
    'widget_tweaks',
    'crispy_forms',
    'bootstrap_modal_forms',
    'global_permissions'
]

LOGGING_MODELS = (
    'modules.base',
    'modules.account',
    'modules.company',
    'django.contrib.auth',
)

CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'PIPELINE_ENABLED': False,
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',
    'COMPILERS': (
        'pipeline.compilers.less.LessCompiler',
        'pipeline.compilers.stylus.StylusCompiler',
    ),
    'JAVASCRIPT': {
        'app': {
            'source_filenames': (
                'js/base_upyexplorer.js',
            ),
            'output_filename': 'js/main.min.js',
        },
        'components': {
            'source_filenames': (
                'js/components/chart.js',
                'js/components/dashboard.js',
                'js/components/hoverable-collapse.js',
                'js/components/jquery.bootstrap.modal.forms.js',
                'js/components/off-canvas.js',
                'js/components/template.js',
            ),
            'output_filename': 'js/components/components.min.js',
        }
    },
    'STYLESHEETS': {
        'styles': {
            'source_filenames': (
                'css/base_upyexplorer.css',
                'css/upy_base.css',
            ),
            'output_filename': 'css/styles.min.css',
        },
    },
}

PIPELINE_DISABLE_WRAPPER = False

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(CONTENT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(CONTENT_DIR, 'tmp/emails')
EMAIL_HOST_USER = os.getenv("DJANGO_EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = os.getenv("DJANGO_DEFAULT_FROM_EMAIL")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sqlite'
    }
}


password_validation = 'django.contrib.auth.password_validation.'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': password_validation + 'UserAttributeSimilarityValidator',
    },
    {
        'NAME': password_validation + 'MinimumLengthValidator',
    },
    {
        'NAME': password_validation + 'CommonPasswordValidator',
    },
    {
        'NAME': password_validation + 'NumericPasswordValidator',
    },
]

ENABLE_USER_ACTIVATION = False
DISABLE_USERNAME = True
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = False
LOGIN_URL = 'account:log_in'
USE_REMEMBER_ME = True

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'account:log_in'

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

SIGN_UP_FIELDS = [
    'username',
    'first_name',
    'last_name',
    'email',
    'password1',
    'password2']

if DISABLE_USERNAME:
    SIGN_UP_FIELDS = [
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'pt-br'
LANGUAGES = [
    ('pt-br', _('Português-BR')),
    ('en', _('English')),
]

TIME_ZONE = 'America/Sao_Paulo'
USE_TZ = True

STATIC_ROOT = os.path.join(CONTENT_DIR, 'staticfiles')
STATIC_URL = '/content/static/'

MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media')
MEDIA_URL = '/content/media/'

STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, 'assets'),
]

LOCALE_PATHS = [
    os.path.join(CONTENT_DIR, 'locale')
]
