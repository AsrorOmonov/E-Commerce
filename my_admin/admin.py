from django.contrib import admin

# Register your models here.
from my_admin.models import TypeModel, BrandModel, OutfitModel


@admin.register(TypeModel)
class TypeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(OutfitModel)
class OutfitModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'created_at']
    list_filter = ['type', 'brand', 'created_at']
    search_fields = ['title', 'summary']
    autocomplete_fields = ['type', 'brand']
