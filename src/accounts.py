from .Hash import HashClass 
from .db.Database import PasswordDatabase
from .exceptions.Exceptions import UserExistsException
from .exceptions.Exceptions import UserDoesNotExistException

global isAuth

db = PasswordDatabase()

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
        except:#?
            print('Error')
        finally:
            return
    
    #TODO: Fix this function
    def checkAuth(self):
        if(self.isAuth):
            return True

        #TODO: use db object to pull username, (hashed) pwd, and salt from accounts table
        
        # print('You must login to continue')
        # print('Username: ')
        # uname = input()
        # print('Password: ')
        # pwd = input()

        try:
            hashTest = db.selectUser(self.uname)
        except UserDoesNotExistException:
            print('Username %s does not exist! ' % self.uname)
        finally:
            return
        

        # count = 0
        # while count < 3:
        #     print('Password: ')
        #     pwd = input()
        #     if(doesPasswordMatch(pwd, check_val)): 
        #         isAuth = True
        #         print('Authenticated!')
        #         return True
        #     elif(count < 2):
        #         print('Incorrect Password! Try again: ')
        #     else:
        #         print('Incorrect Password! Returning to menu')
        #         return False
        #     count = count + 1