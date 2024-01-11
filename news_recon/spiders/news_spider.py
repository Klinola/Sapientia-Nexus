import newspaper
from django.utils import timezone
import pytz
from news_recon.models import Article
from concurrent.futures import ThreadPoolExecutor

class NewsSpider:
    def __init__(self, source_url, max_articles=10):
        self.source_url = source_url
        self.max_articles = max_articles  # 最大文章数量

    def fetch(self):
        print("URL: ", self.source_url)
        source = newspaper.build(self.source_url, memoize_articles=False)
        articles = source.articles[:self.max_articles]  # 限制文章数量
        print("Fetching")
        with ThreadPoolExecutor(max_workers=5) as executor:  # 可以进一步限制线程数
            for article in articles:
                executor.submit(self.process_article, article)

    def process_article(self, article):
        article.download()
        article.parse()
        article.nlp()
        if article.publish_date:
            if article.publish_date.tzinfo is None or article.publish_date.tzinfo.utcoffset(article.publish_date) is None:
                publish_date = pytz.utc.localize(article.publish_date)
            else:
                publish_date = article.publish_date
        else:
            publish_date = timezone.now()
        print("Title: ", article.title)
        print("Summary", article.summary)
        print("Publish Date: ", publish_date)
        if not Article.objects.filter(title=article.title).exists():
            Article.objects.create(
                title=article.title,
                summary=article.summary,
                content=article.text,
                author=', '.join(article.authors),
                publish_date=publish_date,
                url=article.url
            )
