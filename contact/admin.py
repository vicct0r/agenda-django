from django.contrib import admin
from .models import Contato, Category


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'created_date']
    ordering = ['-id']
    list_filter = ['created_date'] 
    search_fields = ['id', 'first_name', 'last_name']
    list_per_page = 10
    list_max_show_all = 100
    #list_editable = ['first_name', 'last_name', 'phone']
    list_display_links = ['first_name', 'id', 'phone']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['id', 'name']
