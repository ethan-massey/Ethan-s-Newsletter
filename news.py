from newsapi import NewsApiClient
import os

# API key
NEWS_KEY = os.environ.get('NEWSAPI_KEY')

# 2D array of articles. Each item is an array containing an article's info:
# [0] = title, [1] = url, [2] = urlToImage
business_articles = []
science_articles = []

def get_news():
    newsapi = NewsApiClient(api_key=NEWS_KEY)

    top_business_headlines = newsapi.get_top_headlines(language='en',
                                              country='us',
                                              category='business')

    top_science_headlines = newsapi.get_top_headlines(language='en',
                                              country='us',
                                              category='science')

    # save business article info
    for i in range(3):
        article_info = []
        article_info.append(top_business_headlines['articles'][i]['title'])
        article_info.append(top_business_headlines['articles'][i]['url'])
        article_info.append(top_business_headlines['articles'][i]['urlToImage'])
        business_articles.append(article_info)

    # save science article info
    for i in range(3):
        article_info = []
        article_info.append(top_science_headlines['articles'][i]['title'])
        article_info.append(top_science_headlines['articles'][i]['url'])
        article_info.append(top_science_headlines['articles'][i]['urlToImage'])
        science_articles.append(article_info)
