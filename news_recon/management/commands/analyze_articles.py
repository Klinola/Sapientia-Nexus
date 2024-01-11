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
            prompt = f"""Please analyze the following article and provide the following details:
            Article: {article.content}

            1. Related Cryptocurrencies:
            2. Sector or Domain:
            3. Importance (0-100):
            4. Urgency (0-100):
            5. Comments and Suggestions:"""
            response = query_chatgpt(prompt, api_key)

            if response.status_code == 200:
                try:
                    response_data = response.json()
                    messages = response_data['choices'][0]['message']['content']  
                    print(messages)
                    analysis_result = messages

                    lines = analysis_result.split('\n')
                    article.related_coins = lines[1].strip()  
                    article.sector = lines[2].strip()        
                    article.importance = int(lines[3].strip()) if lines[3].strip().isdigit() else 0 
                    article.urgency = int(lines[4].strip()) if lines[4].strip().isdigit() else 0    
                    article.comments = lines[5].strip() if len(lines) > 5 else ""    
                    article.is_analyzed = True
                    article.save()
                    self.stdout.write(self.style.SUCCESS(f'Article {article.id} analyzed successfully'))
                except (KeyError, IndexError) as e:
                    self.stdout.write(self.style.ERROR(f'Error parsing response for article {article.id}: {e}'))
            else:
                self.stdout.write(self.style.ERROR(f'API request failed for article {article.id}: Status code {response.status_code}, Response: {response.text}'))
