# coding=utf-8

"""
Module Docstring
"""

from django.contrib import admin
from app.utils import get_field_list
from modules.company.models import (
    CompanyData,
    CompanyConfiguration,
    CompanyRelationship
)


class CompanyDataAdmin(admin.ModelAdmin):
    list_display = get_field_list(CompanyData)


class CompanyConfigurationAdmin(admin.ModelAdmin):
    list_display = get_field_list(CompanyConfiguration)


class CompanyRelationshipAdmin(admin.ModelAdmin):
    list_display = get_field_list(CompanyRelationship)


admin.site.register(CompanyData, CompanyDataAdmin)
admin.site.register(CompanyConfiguration, CompanyConfigurationAdmin)
admin.site.register(CompanyRelationship, CompanyRelationshipAdmin)
