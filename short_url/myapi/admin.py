from django.contrib import admin

from .models import Token
from .forms import TokenForm


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    form = TokenForm
    list_display = ('full_url', 'short_url', 'number_transitions', 'created_at', 'is_active')
    list_filter = ['number_transitions', 'created_at',]

