# coding=utf-8

from django.contrib import admin
from app.utils import get_field_list
from modules.ads.models import (
    AdsLink
)

class AdsLinkAdmin(admin.ModelAdmin):
    list_display = get_field_list(AdsLink)


admin.site.register(AdsLink, AdsLinkAdmin)
