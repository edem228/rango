from django.contrib import admin

# Register your models here.
from . import models
from django_markdown.admin import MarkdownModelAdmin

class ArticleAdmin(MarkdownModelAdmin):
    list_display = ("title", "created_at")
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(models.Article, ArticleAdmin)

