from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    summary = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    url = models.URLField()
