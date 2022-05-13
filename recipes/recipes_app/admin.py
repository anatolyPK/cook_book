from django.contrib import admin

from .models import Recipes


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)

admin.site.register(Recipes, RecipesAdmin)