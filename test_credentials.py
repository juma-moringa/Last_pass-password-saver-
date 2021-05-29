import unittest
from credentials import Credentials ### credentials class being imported

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
    

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credential file.
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_file),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_file = []

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credential
            objects to our credentialredentials
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("POA INTERNET","Jayarlanie","qwertyuiop") # new contact
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_file),2)

    def test_delete_credentials(self):
            '''
            test_delete_credential to test if we can remove a credentials from our credential files
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("POA INTERNET","Jayarlanie","qwertyuiop") # new credential
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credential object
            self.assertEqual(len(Credentials.credentials_file),1)
if __name__ == '__main__':
    unittest.main()    