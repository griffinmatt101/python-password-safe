import bcrypt
import os
import database
from database import PasswordDatabase

global isAuth

class UserAccount:

    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = pwd

    def _doesUserExist(self):
        db = PasswordDatabase()
        return db.dbDoesUserExist(self.uname)

    def addAccount(self):
        
        if(self._doesUserExist()):
            print('Username already exists!')
            #return

        return
        # try:
        #     hash = password_hash(pwd)
        #     print('Account successfully added!')
        # except TypeError:
        #     print('ERROR: Could not add account')
        # finally:
        #     return
    
    #TODO: Fix this function
    def checkAuth(self):
        if(isAuth == True):
            return True

        
        print('You must login to continue')
        print('Username: ')
        uname = input()

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