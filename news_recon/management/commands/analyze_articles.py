import configparser
from django.core.management.base import BaseCommand
from news_recon.models import Article
from news_recon.chatgpt_api import query_chatgpt

class Command(BaseCommand):
    help = 'Analyze articles using ChatGPT API'

    def handle(self, *args, **kwargs):
        config = configparser.ConfigParser()
        #import os
        #from django.conf import settings

        #config_path = os.path.join(settings.BASE_DIR, 'config.ini')
        config.read('config.ini')

        api_key = config['chatgpt']['api_key']
        articles = Article.objects.filter(is_analyzed=False)

        for article in articles[0:5]:
            prompt = (f"Please analyze the following article and provide the following details:\n"
          f"Article: {article.content}\n\n"
          f"1. Related Cryptocurrencies:\n"
          f"2. Sector or Domain:\n"
          f"3. Importance (0-100):\n"
          f"4. Urgency (0-100):\n"
          f"5. Comments and Suggestions:")
            response = query_chatgpt(prompt, api_key)
            analysis_result = response['choices'][0]['text']

            lines = analysis_result.split('\n')
            article.related_coins = lines[1].strip()  # "1. Related Cryptocurrencies:"
            article.sector = lines[2].strip()        # "2. Sector or Domain:"
            article.importance = int(lines[3].strip()) if lines[3].strip().isdigit() else 0  # "3. Importance (0-100):"
            article.urgency = int(lines[4].strip()) if lines[4].strip().isdigit() else 0     # "4. Urgency (0-100):"
            article.comments = lines[5].strip()     # "5. Comments and Suggestions:"
            article.is_analyzed = True
            article.save()

            self.stdout.write(self.style.SUCCESS(f'Article {article.id} analyzed successfully'))