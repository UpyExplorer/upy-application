# coding=utf-8

"""
Source App
"""

import os
import logging

from django.contrib import admin
from django.core.wsgi import get_wsgi_application

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception as error:
    logging.info(error)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application = get_wsgi_application()

admin.site.site_header = 'Backoffice UpyExplorer'
