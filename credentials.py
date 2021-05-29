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