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

    def test_save_user(self):
            '''
            test_save_user test case to test if the user object is saved into the user_list.
            '''
            self.new_user.save_user() # saving the new user
            self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user test case to check if we can save multiple user objects to our user_list.
        '''
        self.new_user.save_user()
        test_user = User("Test","Rachel Owuor","facebook","Owuor@254") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","Rachel Owuor","facebook","Owuor@254") # new user
        test_user.save_user()
        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a user by user name and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","Rachel Owuor","facebook","Owuor@254") # new user
        test_user.save_user()

        found_user = User.find_by_user_name("Rachel Owuor")

        self.assertEqual(found_user.password,test_user.password)





if __name__ == '__main__':
    unittest.main()

