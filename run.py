#!/usr/bin/env python3
from user import User

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

def main():
    print('''
    Hello user, welcome to LASTPASS where we help you remember your credentials
    ''') 
    print("Please enter your Username:") 
    username = input()

    print("Please enter your Password:") 
    password =input()

def main():    
    print("Hello, Welcome to PassworLocker. Create an account to save your passwords")
    print('Enter your username')
    username = input()
    print("What's your password")
    password = input()
    print("Confirm password ....")
    confirm_password = input()
    
    while confirm_password != password:
                print("Password did not match")
                print("password ....")
                password = input()
                print("Confirm password ....")
    else:
                save_user(create_user(username, password))
                print(f'Congratulations 🎉, New Account has been created for: {username} using password: {password}')
                print("proceed to login")
                print("username")
                entered_first_name = input()
                print("your password")
                entered_password = input()            

if __name__ == '__main__':
    main()    