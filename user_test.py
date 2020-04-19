import pyperclip
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

    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly.
            '''

            self.assertEqual(self.new_user.user_name,'Rachel Owuor')
            self.assertEqual(self.new_user.email,'owuorrachel@gmail.com')
            self.assertEqual(self.new_user.account_name,'facebook')
            self.assertEqual(self.new_user.password,'Owuor@254')


if __name__ == '__main__':
    unittest.main()

