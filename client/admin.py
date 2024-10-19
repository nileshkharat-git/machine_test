from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ("client_name", "created_at", "created_by", "updated_at")
    list_filter = ("created_at", "created_by")
    search_fields = ("client_name",)

admin.site.register(Client, ClientAdmin)

