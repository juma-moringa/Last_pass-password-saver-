import random   
import string  
import secrets # import package  
 
def getPasswordLength():
    '''
    retrive the length of a password
    '''
    length = input("Length of your password that you may need: ")
    return int(length)

def passwordGen(length = 8):
    '''
    generates a random password having the specified length
    '''
    password = list(string.ascii_letters + string.punctuation + string.digits)
    random.shuffle(password)
    random_password = ''.join(random.choices(password, k=length))

    return random_password