from celery import shared_task
from .management.commands.save_articles import Command as FetchCommand
from .management.commands.remove_duplicates import Command as RemoveDupCommand
import configparser
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'))

@shared_task
def fetch_and_remove_duplicates():
    websites = config.get('news', 'websites').split(',')
    for website in websites:
        FetchCommand().handle(source_url=website, max_articles = 50)
    RemoveDupCommand().handle()