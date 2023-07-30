from hash import Hash
from db.database import PasswordDatabase

global isAuth

db = PasswordDatabase()

class UserAccount():

    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = pwd

    #TODO: error handling?
    def _doesUserExist(self):
        return db.doesUserExistDB(self.uname)

    def addAccount(self):
        
        if(self._doesUserExist()):
            print('Username already exists!')
            return

        #TODO: use db object to add username, (hashed)pwd, and salt to accounts table
        hashObj = Hash()
        hashObj.newPasswordHash(self.pwd)
        try:
            db.addUser(self.uname,hashObj)
        except:
            print('Error: Unable to add user')
            return
        #TODO: create a new table for new user

        return
    
    #TODO: Fix this function
    def checkAuth(self):
        if(isAuth == True):
            return True

        #TODO: use db object to pull username, (hashed) pwd, and salt from accounts table
        
        print('You must login to continue')
        print('Username: ')
        uname = input()

        count = 0
        while count < 3:
            print('Password: ')
            pwd = input()
            if(doesPasswordMatch(pwd, check_val)): #if password matches what's in the env file
                isAuth = True
                print('Authenticated!')
                return True
            elif(count < 2):
                print('Incorrect Password! Try again: ')
            else:
                print('Incorrect Password! Returning to menu')
                return False
            count = count + 1