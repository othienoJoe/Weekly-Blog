from flask import Flask
from .config import DevConfig

#Let's Initialize the application
app = Flask(__name__)

#Configuration Set Up.
app.config.from_object(DevConfig)

from app import views
