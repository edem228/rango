from django.contrib import admin

# Register your models here.
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    populated_fields = {"slug": ("title",)}
admin.site.register(models.Article)

