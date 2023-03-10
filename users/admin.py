from django.contrib import admin
from .models import CustomUser, BankDetails, HouseAgent

admin.site.site_header ="Hostel App Administration"
admin.site.site_title  =  "Hostel admin"
admin.site.index_title  =  "Admin and staff site only"

class CustomerUserAmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name","is_active", "is_agent")
    list_filter = ("last_name", "last_name")
    
admin.site.register(CustomUser, CustomerUserAmin)
admin.site.register(BankDetails)
admin.site.register(HouseAgent)