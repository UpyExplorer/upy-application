import os
from django.contrib import admin
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application = get_wsgi_application()

admin.site.site_header = 'Backoffice UpyExplorer'