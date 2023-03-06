from django.contrib import admin
from .models import Spice, Comment, TypeCategory


# Register your models here.


@admin.register(TypeCategory)
class TypeCategory(admin.ModelAdmin):
    list_filter = ('category',)
    search_fields = ['category',]
    list_display = ('category',)


@admin.register(Spice)
class Spice(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'type_category', 'use_category',)
    search_fields = ['name', 'type_category', 'use_category',]
    list_display = ('name', 'use_category', 'image',
                    'description', 'price', 'price')


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_filter = ('author', 'spice')
    search_fields = ['author', 'spice']
    list_display = ('author', 'spice', 'body', 'date_created',)
