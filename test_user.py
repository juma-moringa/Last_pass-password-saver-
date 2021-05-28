import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    this is a subclass being created which inherits from unittest testcase
    """
    
        
    def setUp(self):
        """
        this method allows us to define instructions that will be executed before each test
        """

        self.new_user = User("Ajaylee", "ajay254")

    def test_init(self):
        """
        this is a test to check that the objects are correctly instantiated
        """

        self.assertEqual(self.new_user.username,"Ajaylee")
        self.assertEqual(self.new_user.password,"ajay254")

#SECOND TEST save the created accounts details.

    def test_save_user_(self):
        '''
        test_save_user test case to test if the  user object is saved to our
        user list.
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)



if __name__ == '__main__':
    unittest.main()