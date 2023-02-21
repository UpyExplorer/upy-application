import os
# import sentry_sdk
import dj_database_url

from os.path import dirname
from django.utils.translation import gettext_lazy as _
# from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = bool(os.getenv("DJANGO_DEBUG", False))
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

SITE_ID = 1
DISABLE_COLLECTSTATIC = 1

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
    # 'models_logging',
    # Rest Framework
    'rest_framework',
    'rest_framework.authtoken',
]

LOGGING_MODELS = (
    'modules.base',
    'modules.api',
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
    # 'models_logging.middleware.LoggingStackMiddleware',
]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'PIPELINE_ENABLED': True,
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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = os.getenv('DJANGO_DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DJANGO_DATABASE_URL"))
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = False
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'account:log_in'
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = True
EMAIL_ACTIVATION_AFTER_CHANGING = True

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

SIGN_UP_FIELDS = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['first_name', 'last_name', 'email', 'password1', 'password2']

# sentry_sdk.init(
#     dsn="https://1604a98438ee43c79d0a5c421c7c8d75@o1099218.ingest.sentry.io/6123760",
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0,
#     send_default_pii=True
# )
