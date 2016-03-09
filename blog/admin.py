from django.contrib import admin

# Register your models here.
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(models.Article, ArticleAdmin)

