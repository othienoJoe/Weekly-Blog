from flask import Flask

#Let's Initialize the application
app = Flask(__name__)

from app import views
