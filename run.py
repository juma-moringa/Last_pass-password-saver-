#!/usr/bin/env python3
from credentials import Credentials
from user import User
from passGen import *

#####USER#######


def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user


def save_user(User):
    '''
    Function to save contact
    '''
    User.save_user()


def check_existing_user(username, password):
    '''
    Function that check if a user exists with that username and password which returns a Boolean
    '''
    return User.user_exist(username, password)

    ######CREDENTIALS##########


def create_credentials(account, username, password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(account, username, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def delete_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()


def find_credentials(account):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credentials.find_by_username(account)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def check_existing_credentials(account):
    '''
    Function that check if an account exists with the account_name and returns a Boolean
    '''
    return Credentials.credentials_exist(account)


def main():
    print("""
    Hello, Welcome to LAST-PASS!.
    Create an account to save your passwords.
    Here we keep track of your credentials and also help you remember your credentials.
    """)
    while True:
        print('\n')
        print('*-*'*20)
        print('''
        Use these short codes to navigate :
        cu - create a new user,
        lg - login to your account,
        ex -exit the password locker.
           ''')
        print('*-*'*20)

        shortCode = input().lower()

        if shortCode == 'cu':
            print('Enter your username')
            username = input()

            passResponse = input(
                'Do you want a generated password? \n  Respond with \'y\' for yes or \'n\' for no: ').lower()

            if passResponse == 'y':
                createdPass = passwordGen(getPasswordLength())
                password = createdPass

                print(f'''
                New password ({str(len(createdPass))}):
                below...

                {createdPass}
                ''')
            else:

                print("What's your password")
                password = input()
                print("Confirm password ....")
                confirm_password = input()

                while confirm_password != password:
                    print("Password did not match")
                    print("password ....")
                    password = input()
                    print("Confirm password ....")
                    confirm_password = input()

                else:
                    save_user(create_user(username, password))
                    print(
                        f'Congratulations , New Account has been created for: {username} using password: {password}')
                 
        elif shortCode == 'lg':
            print('Enter your username: ')
            defaultUserName = input()

            print('Enter password: ')
            defaultPassword = input()
            print('\n')
            print('Login success! \n')
            print('\n')

            while username != username or password != password:
                print("Missmatch on  username or password")
                print('username')
                entered_username = input()
                print("Your password")
                entered_password = input()
            else:

                print(
                    f'''
                    Welcome back {username}. 
                    Confirmation done successfully.
                        ***@LAST-PASS***

                    ''')

                while True:
                    print('\n')
                    print(
                        '''

                        Use the following short codes to navigate through credentials :
                        ac - add credential,
                        lc - list credentials, 
                        dl - delete credential,
                        ex - exit.(type ex TWICE to exit the application.)

                        ''')
                    print('*'*20)

                    shortCode = input().lower()
                    if shortCode == 'ac':
                        print('*'*20)
                        print('Save new credential...')
                        print('*'*20)
                        print('Enter account to save credentials for: ')
                        credAccount = input()
                        print('*'*20)

                        print('Enter username: ')
                        credUserName = input()
                        print('*'*20)

                        passResponse = input(
                            'Do you want a generated password? \n  Respond with \'y\' for YES or \'n\' for NO: ').lower()

                        if passResponse == 'y':
                            createdPass = passwordGen(getPasswordLength())
                            confirmedPass = createdPass

                            save_credentials(create_credentials(
                                credAccount, credUserName, createdPass))
                            print(
                                f'''
                                                New password ({str(len(createdPass))}):  
                                                below
                                                {createdPass}
                                                ''')
                        else:
                            print('Enter password: ')
                            credPass = input()

                            print('Comfirm password: ')
                            confirmedPass = input()

                            print('\n')

                            if credPass != confirmedPass:
                                print('MISMATCH!!!! .....  invalid password')
                                print('Enter password: ')
                                credPass = input()

                                print('Confirm password: ')
                                confirmedPass = input()
                            else:
                                save_credentials(create_credentials(
                                    credAccount, credUserName, credPass))
                                print(
                                    f'''
                                    Congratulations {username},your credentials for {credAccount} was successfully created!.
                                                              *****@LAST-PASS*****
                                    ''')
                                print('\n')


                    
                    elif shortCode == 'lc':
                        if display_credentials():
                            print('Here is a list of all your contacts')
                            print('\n')
                            for credential in display_credentials():
                                print(
                                    f'{credential.account}: \n user name: {credential.username}, password: {credential.password}')

                            print('\n')
                        else:
                            print('\n')
                            print("We cant find the credential....it seems you have no credentials available")
                            print('\n')

                    elif shortCode == 'dl':
                        print("Enter name of account to be deleted")
                        account = input()
                        if check_existing_credentials(account):
                            print("Please wait ...")
                            account = find_credentials(
                                account)
                            delete_credentials(account)
                            print(
                                f"Account {username.credentials}deleted successfully")
                        else:
                            print('\n')
                            print("delete failed")

                    elif shortCode == 'ex':
                        break

                    else:
                     print('Invalid credentials short code')
        elif shortCode == 'ex':
            print("""

                 Bye thank you for choosing last-pass...
                       ***@LAST-PASS***
                       Jaycreations 2021

            """)
            break

if __name__ == '__main__':
    main()


