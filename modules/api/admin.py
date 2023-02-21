# coding=utf-8

"""
Module Docstring
"""

from django.contrib import admin
from app.utils import get_field_list
from modules.api.models import (
    Token
)


class TokenAdmin(admin.ModelAdmin):
    list_display = get_field_list(Token)


admin.site.register(Token, TokenAdmin)
