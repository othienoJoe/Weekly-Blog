from flask import render_template, request, redirect, url_for
from app import app
from ..request import get_news,get_news, search_news_articles

# The views
@app.route('/')
def index():
	"""
	This is the view root page that returns the index page and its data.
	"""

	# Getting the most popular news
	popular_news = get_news('articles')
	print(popular_news)
	trending_news = get_news('now_trending')
	title = 'Home - Welcome to People Favorite News Site'

	search_news_articles = request.args.get(news)

	if search_news_articles:
		return redirect(url_for('search', news_title = search_news_articles))
	else:
	  return render_template('index.html', title = title, popular = popular_news, now_trending = trending_news)

@app.route('/news/<int:news_id>')
def news(news_id):
	"""
	A function for the news that returns the news' details and it data.
	"""
	news = get_news(news_id)
	print(news)
	title = f'{news_id}'

	return render_template('news.html', title = title, news = news)
