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