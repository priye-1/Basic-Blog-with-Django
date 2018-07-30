
"""Coordinates Admin Configuration  for the Post module"""
from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Represents admin view configuration for post model"""
    fields = ('title', 'publisher', 'is_draft',
              'date_published', 'content', 'headline', 'picture')
    list_display = ('title', 'publisher', 'is_draft', 'picture',
                    'date_published', 'date_created', 'last_updated')
    list_filter = ('publisher', 'is_draft',
                   'date_published', 'last_updated')


# @admin.register(Post)
# class SearchAdmin(admin.ModelAdmin):
#     search_fields = ('name', 'description', 'keyword', )
