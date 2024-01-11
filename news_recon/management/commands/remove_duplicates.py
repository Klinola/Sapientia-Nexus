from django.core.management.base import BaseCommand
from django.db.models import Count
from news_recon.models import Article

class Command(BaseCommand):
    help = 'Remove duplicate articles from the database'

    def handle(self, *args, **kwargs):
        seen_titles = set()
        for article in Article.objects.all().order_by('publish_date').iterator():
            if article.title in seen_titles:
                article.delete()
            else:
                seen_titles.add(article.title)


        self.stdout.write(self.style.SUCCESS('Successfully removed duplicate articles'))

