from django.shortcuts import render
from .models import Article

def news_list(request):
    articles = Article.objects.all().order_by('-publish_date')  # 获取所有文章并按发布日期降序排列
    return render(request, 'news_recon/news_list.html', {'articles': articles})
