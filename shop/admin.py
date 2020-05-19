from django.contrib import admin
from .models import Article, Category


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('content', 'title')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Article, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)

