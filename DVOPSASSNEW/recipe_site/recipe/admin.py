from django.contrib import admin
from .models import Recipe, Video

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipe', 'uploaded_at')
    search_fields = ('title', 'recipe__title')
