from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "name", "email", "phone", "date")
    list_display_links = ("id", "title", "name", "email", "phone")
    list_per_page = 30


admin.site.register(Contact, ContactAdmin)