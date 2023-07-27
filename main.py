# Python Password Safe Main File

from pass_hash import *
from database import *

def main():

    print('This program is designed to test password hashing and database storage.')
    print('Please select an option: ')
    print('1. Create New Entry')
    print('2. Retrieve Entry')
    x = input()
    # need type and error checking
    if(x == '1'):
        print('Enter the name of the site or application associated with this password')
        name = input()
        print('Enter the password you want to store: ')
        pwd = input()
        #need encryption function
        
    elif(x == '2'):
        #will need to see if you are already authenticated (can be done in function)
        print('Enter the name of the site or application you want to retrieve the password for: ')
        name = input()

    elif (x == '3'):
        #test db connection
        db_con()

if __name__ == "__main__":
    main()