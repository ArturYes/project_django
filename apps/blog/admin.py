from django.contrib import admin

from apps.blog.models import Article


@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_publication', 'count_views',)
    list_filter = ('title',)
    search_fields = ('title',)
