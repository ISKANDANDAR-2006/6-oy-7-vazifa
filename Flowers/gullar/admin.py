from django.contrib import admin

from django.contrib import admin
from .models import Type, Flower

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'description')
    search_fields = ('name', 'type__name')
    list_filter = ('type',)
