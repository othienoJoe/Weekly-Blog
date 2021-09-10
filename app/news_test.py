import unittest
from models import news
News = news

class NewsTest(unittest.TestCase):
	"""
	This Test Class tests the behavior of the News Class.
	"""
	def setUp(self):
		'''
		A set up method that will run before every test.
		'''
		self.recent_news = News(1234, 'President Kenyatta Resigns', 'Western Region Under Flood Treat', 'file:///home/moringa/Pictures/Maguire.png', 4.6, 30828344)

	def test_instance(self):
		self.assertTrue(isinstance(self.recent_news,News))

if __name__ == '__main':
	unittest.main()
