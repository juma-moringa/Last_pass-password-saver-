import unittest
from credentials import Credentials ### credentials class being imported
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    TEST class which defines the test cases for credentials

    '''
    def setUp(self):
        '''
        set up method to to run before each test case.
        '''
        self.new_credentials = Credentials('Twitter','Ajaylee254','jay254')
    def test_init(self):
        '''
        test init  test case  to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account,'Twitter')  
        self.assertEqual(self.new_credentials.username,'Ajaylee254')
        self.assertEqual(self.new_credentials.password,'jay254')
    
    #test 1
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credential file.
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_file),1)

        #test4
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_file = []

        #test2
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credential
            objects to our credentialredentials
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("POA INTERNET","Jayarlanie","qwertyuiop") # new contact
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_file),2)

        #test3
    def test_delete_credentials(self):
            '''
            test_delete_credential to test if we can remove a credentials from our credential files
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("POA INTERNET","Jayarlanie","qwertyuiop") # new credential
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credential object
            self.assertEqual(len(Credentials.credentials_file),1)

        #test5
    def test_find_credentials_by_username(self):
        '''
        test to check if we can find a credential usredentials and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("POA INTERNET","Jayarlanie","qwertyuiop") # new credential
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_username("Jayarlanie")

        self.assertEqual(found_credentials.password,test_credentials.password)

        #test6
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved in the file.
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_file)

       #test7
    def test_exist_credentials(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("POA INTERNET","Jayarlanie","qwertyuiop") # new crederedentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("POA INTERNET","Jayarlanie","qwertyuiop")

        self.assertTrue(credentials_exists) 

      #test7 will get back to it later
    # def test_copy_credentials(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found credential
    #     '''

    #     self.new_credentials.save_credentials()
    #     Credentials.username("Ajaylee254")
    #     Credentials.password("jay254")
        

    #     self.assertEqual(self.new_credentials.username,pyperclip.paste())
    #     self.assertEqual(self.new_credentials.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()    