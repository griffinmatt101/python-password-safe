# Python Password Safe Main File

from pass_hash import *

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
        password_hash(name,pwd)
    elif(x == '2'):
        #will need to see if you are already authenticated
        if()
        print('Enter the name of the site or application you want to retrieve the password for: ')
        name = input()


if __name__ == "__main__":
    main()