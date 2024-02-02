from django.contrib import admin
from . models import ContactModel
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']
    
admin.site.register(ContactModel,ContactAdmin)
