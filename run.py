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
