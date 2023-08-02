# Python Password Safe Main File
from src.Accounts import UserAccount
from src.Service import ServiceClass
from src.Accounts import db

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
    while x != 'q': 
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
                if(account.checkAuth()):
                    print('AUTHED')
                    isAuth = account.isAuth
                else:
                    print('Please select an option: ')
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