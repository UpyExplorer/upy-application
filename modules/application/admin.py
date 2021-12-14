from django.contrib import admin
from modules.application.models import (
   BaseApplication,
   ApplicationLink
)

class BaseApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'key', 'description', 'url']


class ApplicationLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'base_application', 'company_data', 'creation_time']


admin.site.register(BaseApplication, BaseApplicationAdmin)
admin.site.register(ApplicationLink, ApplicationLinkAdmin)
