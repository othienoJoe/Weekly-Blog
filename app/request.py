from app import app
import urllib.request,json
from .models import Sources, Articles

# Generating tha api key
api_key = 'ddbdb92d9552495e8799450b31bee0ff'

# Getting the news base url
base_url_source = None

base_url_articles = None

def configure_request(app):
    global api_key, base_url_source, base_url_articles
    base_url_source = app.config['NEWS_API_SOURCE_URL']
    base_url_articles = app.config['NEWS_API_ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']

# Getting the news articles by their id
def get_news(news_id):
	get_news_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(news_id, api_key)
	print(get_news_url)

	with urllib.request.urlopen(get_news_url) as url:
		news_details_data = url.read()
		news_details_response = json.loads(news_details_data)

		news_results = None

		if news_details_response['articles']:
			news_results_list = news_details_response['articles']
			news_results = process_results(news_results_list)

	return news_results

def get_news(category):
	'''
	This function gets the json response to our url request
	'''
	get_news_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(category, api_key)

	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = None

		if get_news_response['articles']:
			news_results_list = get_news_response['articles']
			news_results = process_results(news_results_list)

	return news_results

def process_results(articles_list):
	'''
	This function processes the news result and transform then to the lost of Objects
	Args:
	  news_list: A list of news Objects.
	'''
	articles_results = []
	for news_item in articles_list:
		author = news_item.get('author')
		title = news_item.get('title')
		description = news_item.get('description')
		url = news_item.get('url')
		urlToImage = news_item.get('urlToImage')
		publishedAt = news_item.get('publishedAt')
		content = news_item.get('content')

		if urlToImage:
			articles_object = Articles(author, title, description, url, urlToImage, publishedAt, content)
			articles_results.append(articles_object)

	return articles_results

# Process the Resulting News
def process_results(news_list):
	'''
	This function processes the news result and transform then to the lost of Objects
	Args:
	  news_list: A list of news Objects.
	'''
	news_results = []
	for news_item in news_list:
		author = news_item.get('author')
		title = news_item.get('title')
		description = news_item.get('description')
		url = news_item.get('url')
		urlToImage = news_item.get('urlToImage')
		publishedAt = news_item.get('publishedAt')
		content = news_item.get('content')

		news_object = Sources(author, title, description, url, urlToImage, publishedAt, content)
		news_results.append(news_object)

	return news_results

# To Get News From A Specific Source and Page Size
def  search_news_articles(source, pageSize):
	search_news_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(source, api_key, pageSize)

	with urllib.request.urlopen(search_news_url) as url:
		search_news_data = url.read()

		get_articles_response = json.loads(search_news_data)

		news_results = None

		if get_articles_response['articles']:
			news_results_list = get_articles_response['articles']
			news_results = process_results(news_results_list)

	return news_results
