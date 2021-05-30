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
    def find_by_account(cls, account):
        '''
        Method that takes in a account name and returns a credentials that matches that account.

        Args:
            account: account to search for
        Returns :
            Credentials of account that matches the account.
        '''

        for credentials in cls.credentials_file:
            if credentials.account == account:
                return credentials

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credentials_file 

    def credentials_exist(cls, account):
        '''
         Method that checks if a account exists from the credentials list.
        Args:
            string: account name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for credentials in cls.credentials_file:
            if credentials.account == account:
                return True

        return False
   

     