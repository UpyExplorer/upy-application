# coding=utf-8

"""
Module Docstring
"""

from django.contrib import admin
from app.utils import get_field_list
from modules.application.models import BaseApplication, ApplicationLink


class BaseApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'description',
        'url',
        'type',
        'Installed',
        'stars',
        'status']


class ApplicationLinkAdmin(admin.ModelAdmin):
    list_display = get_field_list(ApplicationLink)


admin.site.register(BaseApplication, BaseApplicationAdmin)
admin.site.register(ApplicationLink, ApplicationLinkAdmin)
