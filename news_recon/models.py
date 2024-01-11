from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    summary = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    url = models.URLField()
    is_analyzed = models.BooleanField(default=False)
    comments = models.TextField(blank=True)
    related_coins = models.CharField(max_length=200, blank=True)  # 相关币种
    sector = models.CharField(max_length=200, blank=True)  # 板块领域
    importance = models.IntegerField(default=0)  # 重要性（100分制）
    urgency = models.IntegerField(default=0)  # 紧急程度（100分制）
