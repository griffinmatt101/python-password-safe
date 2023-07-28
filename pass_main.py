import bcrypt
import os
import dotenv
from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

global isAuth
# load .env file
dotenv_file = join(dirname(__file__), ".env")
load_dotenv(dotenv_file)

def addAccount(uname,pwd):
    for entries in environ:
        if(uname == entries):
            print('Username already exists!')
            return

    hash = password_hash(pwd)
    #environ[uname] = hash
    dotenv.set_key(dotenv_file, uname, hash)
    print('Account successfully added!')
    
def check_auth():
    if(isAuth == True):
        return True

    print('You must login to continue')
    print('Username: ')
    uname = input()
    check_val = dotenv.get_key(dotenv_file, uname) #returns hash value

    count = 0
    while count < 3:
        print('Password: ')
        pwd = input()
        if(check_password(pwd, check_val)): #if password matches what's in the env file
            isAuth = True
            print('Authenticated!')
            return True
        elif(count < 2):
            print('Incorrect Password! Try again: ')
        else:
            print('Incorrect Password! Returning to menu')
            return False
        count = count + 1

# Method to create a new password hash
def password_hash(pwd):
    #convert password to array of bytes
    bytes = pwd.encode('utf-8')

    #generate salt
    salt = bcrypt.gensalt()

    #hash password
    hash = bcrypt.hashpw(bytes, salt)

    return hash
    #for testing, store in global array
    #global stored_hash = {}

def check_password(pwd, check_val):
    hash = password_hash(pwd)

    result = bcrypt.checkpw(check_val,hash)

    return result