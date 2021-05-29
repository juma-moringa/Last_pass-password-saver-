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


if __name__ == '__main__':
    unittest.main()    