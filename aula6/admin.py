from django.contrib import admin
from .models import Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    search_fields = ['first_name']


admin.site.register(Contato, ContatoAdmin)
