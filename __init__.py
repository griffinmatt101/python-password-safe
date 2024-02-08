# Python Password Safe Main File
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/src")

from Accounts import UserAccount
from Service import ServiceClass
from Accounts import db

def menu():
    print('This program is designed to test password encryption and database storage.')
    print('Please select an option: ')
    print('1. New Python Password Account')
    print('2. Create New Entry')
    print('3. Retrieve Entry')
    print('0. Display main menu options')
    print('Press Q to quit')

def main():
    isAuth = False
    menu()
    x = ''
    while True: 
        x = input()
        #TODO: Error and Type checking

        # NEW ACCOUNT --------------------------------------------------
        if(x == '1'):
            print('Please enter the USERNAME you would like to create')
            uname = input()
            print('Please enter the PASSWORD you would like to create')
            pwd = input()
            account = UserAccount(uname,pwd)
            account.addAccount()
            print('Please select an option: ')
        # --------------------------------------------------------------

        # NEW ENTRY -----------------------------------
        elif(x == '2'):
            #check auth first
            if(not isAuth):
                print('You must login to continue')
                print('Username')
                uname = input()
                print('Password')
                pwd = input()

                account = UserAccount(uname,pwd)
                hashComp = account.selectAccount()
                
                count = 0
                while count < 3:
                    if(hashComp == None):
                        print('Returning to menu')
                        break
                    elif(account.checkAuth(hashComp)):
                        print('AUTHED')
                        isAuth = account.isAuth
                        break
                    elif (count < 2):
                        print('Incorrect Password! Try again: ')
                        account.pwd = input()
                    else:
                        print('Incorrect Password! Returning to menu')
                    count = count + 1
        # ---------------------------------------------

        # RETRIEVE ENTRY ------------------------------------------------------------------------------
        elif(x == '3'):
            #will need to see if you are already authenticated (can be done in function)
            print('Enter the name of the site or application you want to retrieve the password for: ')
            name = input()
        # ---------------------------------------------------------------------------------------------

        # MENU -------------------------------------
        elif (x == '0' or x == 'h' or x == 'help'):
            menu()
        # ------------------------------------------

        # QUIT -----------------------------------------
        elif (x.upper() == 'Q' or x.upper() == 'QUIT'):
            print('Goodbye!')
            db.closeDB()
            break
        # ----------------------------------------------

        # ERROR -------------------------------------
        else:
            print('Please enter the correct input')
            print('Display menu options with 0')
        # -------------------------------------------

if __name__ == "__main__":
    main()


'''
FIX USER INPUT
EXAMPLE:
def getNumeric(prompt):
    while True:
        try:
            res = int(input(prompt))
            break
        except ValueError:
            print("Numbers only please!")
    return res
'''