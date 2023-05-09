from django.contrib import admin

from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('full_url', 'short_url', 'number_transitions', 'created_at', 'is_active')


