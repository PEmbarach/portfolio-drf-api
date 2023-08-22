from django.contrib import admin
from .models import message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'company', 'message')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'company')
    list_per_page = 25

admin.site.register(message, MessageAdmin)
