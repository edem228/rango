from django.db import models

# Create your models here.
class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published_at = True)


class Article(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    slug = models.SlugField(max_length = 200, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    published = models.BooleanField(default = True)
    modified_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-created_at"]

