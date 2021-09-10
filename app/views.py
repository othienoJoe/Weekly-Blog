from flask import render_template
from app import app

# The views
@app.route('/')
def index():
	"""
	This is the view root page that returns the index page and its data.
	"""
	message = 'Hello World'
	return render_template('index.html', message = message)

@app.route('/news/<int:news_id>')
def news(news_id):
	"""
	A function for the news that returns the news' details and it data.
	"""
	return render_template('news.html',id = news_id)
	