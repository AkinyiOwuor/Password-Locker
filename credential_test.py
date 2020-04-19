import pyperclip
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.
    unittest.Testcase class helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential=Credential('Rachel Owuor','facebook','Owuor@254','owuorrachel@gmail.com')

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Rachel Owuor")
        self.assertEqual(self.new_credential.account_name,"facebook")
        self.assertEqual(self.new_credential.password,"Owuor@254")
        self.assertEqual(self.new_credential.email,"owuorrachel@gmail.com")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credential list.
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1) 



