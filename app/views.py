from flask import render_template
from app import app

# The views
@app.route('/')
def index():
	"""
	This is the view root page that returns the index page and its data.
	"""
	return render_template('index.html')