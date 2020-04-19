import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''
        Set up method that will run before each test cases.
        '''
        self.new_user=User('Rachel Owuor','owuorrachel@gmail.com','facebook','Owuor@254')
