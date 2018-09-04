import unittest # Importing the unittest module
from app.models import Articles, Sources # Importing the contact class

class TestArticles(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('Floods','cnn','life in bangladesh','image','8.5129993')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

class TestSources(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources(1,'name','life in bangladesh','www.bbc.com','general','english','country')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))
