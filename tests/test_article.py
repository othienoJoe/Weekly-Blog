import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
  def setUp(self):
    self.new_article = Articles('CNN',
																'A West Virginia city is taking a Tesla patrol car for a test drive',
																'Emma Raducanu defeats Leylah Fernandez in all-teen US Open final',
																'The strangers who fell in love when 9/11 diverted their flight',
																'https://twitter.com/cnnbrk/status/1436882485170802688','2019-09-04T14:00:00Z',
                                "SLIDELL, La. -- A man was attacked by a large alligator while walking through floodwaters from Hurricane Ida and is now missing, a Louisiana sheriff said.\r\nThe 71-year-old mans wife told sheriffs dep… [+1041 chars]"
                                    )

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Articles))