from flask import render_template
from app import app

# The views
@app.route('/')
def index():
	"""
	This is the view root page that returns the index page and its data.
	"""
	title = 'Home - Welcome to Number 0ne(1) News Site'
	return render_template('index.html', title = title)

@app.route('/news/<int:news_id>')
def news(news_id):
	"""
	A function for the news that returns the news' details and it data.
	"""
	return render_template('news.html',id = news_id)
