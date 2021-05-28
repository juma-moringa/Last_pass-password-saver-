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

if __name__ == '__main__':
    main()    