from django.contrib import admin
from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    emptty_value_displaye = "empty"
    list_display=("name","subject","email","create_date")
    search_fields=("name",)