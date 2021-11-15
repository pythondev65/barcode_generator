from django.contrib import admin
from home.models import signup_data,barcode

# Register your models here.
class signupadmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","email","phonenumber","username","password"]
admin.site.register(signup_data,signupadmin)

admin.site.register(barcode)