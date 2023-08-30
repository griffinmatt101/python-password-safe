import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/src")

from Hash import HashClass 
from db.Database import PasswordDatabase
from exceptions.Exceptions import UserExistsException
from exceptions.Exceptions import UserDoesNotExistException
from exceptions.Exceptions import DatabaseErrorException

global isAuth

db = PasswordDatabase()

'''
Class to hold username, password, and whether they are currently authenticated
'''
class UserAccount:

    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = pwd
        self.isAuth = False

    '''
    Creates hash object that stores the hashed password and unique salt,
    add user, pwd, salt to database, return to main
    '''
    def addAccount(self):

        hashObj = HashClass()
        hashObj.newPasswordHash(self.pwd)
        
        try:
            db.addUser(self.uname,hashObj)
        except UserExistsException:
            print('Username already exists!')
        except DatabaseErrorException:
            print('Database error')
        finally:
            return

    '''
    
    '''
    def addEntry(self):
        return
    
    '''
    Grabs password and hash from database for username, and compares with
    the provided password to see if hashes match
    '''
    def checkAuth(self):

        if(self.isAuth):
            return True

        try:
            hashTest = db.selectUser(self.uname)
        except UserDoesNotExistException:
            print('Username %s does not exist! ' % self.uname)
            return
        except DatabaseErrorException:
            print('Database Error')
            return

        count = 0

        while count < 3:
            if(hashTest.checkHashWithSalt(self.pwd)): 
                self.isAuth = True
                print('Authenticated!')
                return True
            elif(count < 2):
                print('Incorrect Password! Try again: ')
                self.pwd = input()
            else:
                print('Incorrect Password! Returning to menu')
                return False
            count = count + 1