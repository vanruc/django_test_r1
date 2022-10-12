from django.contrib import admin
from .models import Store, Leads

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'store_name',
        'store_owner',
        'website_url',
        'city',
        'country'
    ]
    list_filter = ['country',]
    search_fields = ['store_name', 'website_url']


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = [
        'store',
        'email_address',
        'status'
    ]
    list_filter = ['status','store']
    search_fields = ['email_address']
