from django.contrib import admin
from .models import CustomUser

admin.site.site_header ="Hotel App Administration"
admin.site.site_title  =  "Hostel admin"
admin.site.index_title  =  "Admin and staff site only"

class CustomerUserAmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name","is_active")
    list_filter = ("last_name", "last_name")
    
admin.site.register(CustomUser, CustomerUserAmin)