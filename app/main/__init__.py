from flask import Blueprint
from flask.app import Flask
main = Blueprint('main', __name__)
from . import views, error
