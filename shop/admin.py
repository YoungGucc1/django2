from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Article, Category


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('content', 'title')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category',)
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at', 'get_photo')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '_'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Article, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)
