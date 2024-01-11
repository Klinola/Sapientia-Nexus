from django.core.management.base import BaseCommand
from news_recon.spiders.news_spider import NewsSpider

class Command(BaseCommand):
    help = 'Fetch and save articles from a news source'

    def add_arguments(self, parser):
        parser.add_argument('source_url', type=str, help='URL of the news source')
        parser.add_argument('--max_articles', type=int, default=10, help='Maximum number of articles to fetch')

    def handle(self, *args, **kwargs):
        source_url = kwargs['source_url']
        max_articles = kwargs['max_articles']
        spider = NewsSpider(source_url, max_articles)
        spider.fetch()
        self.stdout.write(self.style.SUCCESS(f'Successfully saved articles from {source_url}'))