from flask import render_template
from app import app
from .request import get_news,get_news

# The views
@app.route('/')
def index():
	"""
	This is the view root page that returns the index page and its data.
	"""

	# Getting the most popular news
	popular_news = get_news('popular')
	print(popular_news)
	trending_news = get_news('now_trending')
	title = 'Home - Welcome to People Favorite News Site'
	return render_template('index.html', title = title, popular = popular_news, now_trending = trending_news)

@app.route('/news/<int:news_id>')
def news(news_id):
	"""
	A function for the news that returns the news' details and it data.
	"""
	return render_template('news.html',id = news_id)
