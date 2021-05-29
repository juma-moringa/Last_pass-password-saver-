import pyperclip
class Credentials:
    '''
    class that gets new instances of credentials
    '''

    credentials_file=[]
    def __init__(self,account,username, password):
        '''
        method that helps us define properties for our objects.

        '''

        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credential objects into credentials_file
        '''

        Credentials.credentials_file.append(self) 

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credential from the credential_file
        '''

        Credentials.credentials_file.remove(self)  

    @classmethod
    def find_by_username(cls, username):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credentials in cls.credentials_file:
            if credentials.username == username:
                return credentials

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credentials_file 


        #come back
    # @classmethod
    # def copy_credentials(cls,username,password):
    #     credentials_found = Credentials.find_by_username(username, password)
    #     pyperclip.copy(credentials_found.username, credentials_found.password)               