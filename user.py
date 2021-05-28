class User:
    """
    Class that generates instance of user...

    """
    user_list =[]
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self) 

    @classmethod
    def user_exist(cls,username, password):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user  in cls.user_list:
            if (user.username == username and user.password == password):
                    return True

        return False  