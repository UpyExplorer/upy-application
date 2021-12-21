from django.contrib import admin
from app.base import get_field_list
from modules.advertising.models import (
    AdvertisingLink
)

class AdvertisingLinkAdmin(admin.ModelAdmin):
    list_display = get_field_list(AdvertisingLink)


admin.site.register(AdvertisingLink, AdvertisingLinkAdmin)
