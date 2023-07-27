# Python Password Safe Main File

from pass_hash import *

def main():
    print('This program is designed to test password hashing and database storage.')
    print('Please select an option: ')
    print('1. Create new Password')
    print('2. Update Password')
    print('3. Retrieve Password')
    x = input()
    # need type and error checking
    if(x == '1'):
        print('Enter the password you want to create: ')
        x = input()
        password_hash(x)
    # elif(x == '2'):

    # elif(x == '3'):

    # else:
    #     print('Input error!')

if __name__ == "__main__":
    main()