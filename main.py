# Python Password Safe Main File

# * is just for testing
from pass_main import *
from database import *

def menu():
    print('This program is designed to test password encryption and database storage.')
    print('Please select an option: ')
    print('1. New Python Password Account')
    print('2. Create New Entry')
    print('3. Retrieve Entry')
    print('0. Display main menu options')

def main():

    isAuth = False
    menu()
    x = ''
    while x != 'q': 
        x = input()
        # need type and error checking

        # NEW ACCOUNT ##################################################
        if(x == '1'):
            print('Please enter the USERNAME you would like to create')
            uname = input()
            print('Please enter the PASSWORD you would like to create')
            pwd = input()
            addAccount(uname,pwd)
        ################################################################

        # NEW ENTRY #########################################################################
        elif(x == '2'):
            #check auth first
            if(not isAuth):
                if(check_auth()):
                    print('Enter the name of the SITE or APPLICATION associated with this password')
                    uname = input()
                    print('Enter the PASSWORD you want to store: ')
                    pwd = input()
                    #need encryption function
        #####################################################################################

        # RETRIEVE ENTRY ##############################################################################
        elif(x == '3'):
            #will need to see if you are already authenticated (can be done in function)
            print('Enter the name of the site or application you want to retrieve the password for: ')
            name = input()
        ###############################################################################################

        # MENU #####################################
        elif (x == '0' or x == 'h' or x == 'help'):
            menu()
        ############################################

        # QUIT ######################
        elif (x == 'q' or x == 'Q'):
            print('Goodbye!')
            break
        #############################

        elif(x == 'db'):
            db_con()

        # ERROR #####################################
        else:
            print('Please enter the correct input')
            print('Display menu options with 0')
        #############################################

if __name__ == "__main__":
    main()