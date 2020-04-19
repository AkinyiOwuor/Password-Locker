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

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","Rachel Owuor","facebook","owuorrachel@gmail.com") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_delete_contact(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list.
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","Rachel Owuor","facebook","owuorrachel@gmail.com") # new credential
        test_credential.save_credential()
        self.new_credential.delete_credential()# Deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_account_name(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","Rachel Owuor","facebook","owuorrachel@gmail.com") 
        test_credential.save_credential()

        found_credential = Credential.find_by_account_name("facebook")

        self.assertEqual(found_credential.email,test_credential.email)

    def test_credential_exists(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","Rachel Owuor","facebook","owuorrachel@gmail.com") # new contact
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("facebook")

        self.assertTrue(credential_exists)

    





if __name__ == '__main__':
    unittest.main()



