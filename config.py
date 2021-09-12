# from instance.config import NEWS_API_KEY
import os

class Config:
	'''
	General configuration parent class
	'''
	NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
	NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
	NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string here it is'

	@staticmethod
	def init_app(app):
		pass

class ProdConfig(Config):
	'''
	Production  configuration child class

	Args:
			Config: The parent configuration class with General configuration settings
	'''
	pass

class DevConfig(Config):
	'''
	Development  configuration child class

	Args:
			Config: The parent configuration class with General configuration settings
	'''
	DEBUG = True

config_map = {
	'development' : DevConfig,
	'production' : ProdConfig
}