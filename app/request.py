from app import app
import urllib.request,json
from .models import news

News = news.News

# Generating tha api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_KEY_BASE_URL"]

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
