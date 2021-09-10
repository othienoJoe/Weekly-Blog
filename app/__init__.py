from flask import Flask
from .config import DevConfig

#Let's Initialize the application
app = Flask(__name__, instance_relative_config = True)

#Configuration Set Up.
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
