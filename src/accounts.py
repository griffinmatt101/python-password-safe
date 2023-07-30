from .Hash import HashClass 
from .db.Database import PasswordDatabase

global isAuth

db = PasswordDatabase()

class UserAccount:

    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = pwd

    '''
    This function first checks if the user already exists in the database

    If user exists --> return to main
    
    If user does not exist --> create hash object that stores the hashed password and unique salt,
    add user, pwd, salt to database, return to main
    '''
    def addAccount(self):

        hashObj = HashClass()
        hashObj.newPasswordHash(self.pwd)

        try:
            db.addUser(self.uname,hashObj)
        except UserExistsException:
            print('Username already exists account level')
            #print('Error: Unable to add user')
        except:
            print('Error')
        finally:
            return
    
    #TODO: Fix this function
    # def checkAuth(self):
    #     if(isAuth == True):
    #         return True

    #     #TODO: use db object to pull username, (hashed) pwd, and salt from accounts table
        
    #     print('You must login to continue')
    #     print('Username: ')
    #     uname = input()

    #     count = 0
    #     while count < 3:
    #         print('Password: ')
    #         pwd = input()
    #         if(doesPasswordMatch(pwd, check_val)): #if password matches what's in the env file
    #             isAuth = True
    #             print('Authenticated!')
    #             return True
    #         elif(count < 2):
    #             print('Incorrect Password! Try again: ')
    #         else:
    #             print('Incorrect Password! Returning to menu')
    #             return False
    #         count = count + 1