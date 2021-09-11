from instance.config import NEWS_API_KEY

class Config:
	'''
	General configuration parent class
	'''
	NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=apple&from=2021-09-09&to=2021-09-09&sortBy=popularity&apiKey=ddbdb92d9552495e8799450b31bee0ff'

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
