from app import app
import urllib.request,json
from .models import news

News = news.News

# Generating tha api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
	'''
	This function gets the json response to our url request
	'''
	get_news_url = base_url(category,api_key)

	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = None

		if get_news_response['results']:
			news_results_list = get_news_response['results']
			news_results = process_results(news_results_list)

	return news_results

def process_results(news_list):
	'''
	This function processes the news result and transform then to the lost of Objects
	Args:
	  news_list: A list of news Objects.
	'''
	news_results = []
	for news_item in news_list:
		id = news_item.get('id')
		title = news_item.get('original_title')
		overview = news_item.get('overview')
		poster = news_item.get('poster_path')

		if poster:
			news_object = News(id,title,overview,poster)
			news_results.append(news_object)

	return news_results
