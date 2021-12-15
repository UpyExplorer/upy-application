from django.contrib import admin
from app.base import get_field_list
from modules.customer.models import (
    Customer
)

class CustomerAdmin(admin.ModelAdmin):
    list_display = get_field_list(Customer)


admin.site.register(Customer, CustomerAdmin)
