import bcrypt
import keyring
import keyring.util.platform_ as keyring_platform

global isAuth

def addAccount(uname,pwd):
    # TODO: CHECK IF USERNAME EXISTS FIRST

    # TODO: HASH PASSWORD
    # TODO: ADD TO KEYRING

def check_auth():
    if(isAuth == True):
        return True

    print('You must login to continue')
    print('Username: ')
    uname = input()
    print('Password: ')
    pwd = input()

    #TODO: VALIDATE WITH KEYRING


# Method to create a new password hash
def password_hash(pwd):
    #convert password to array of bytes
    bytes = pwd.encode('utf-8')

    #generate salt
    salt = bcrypt.gensalt()

    #hash password
    hash = bcrypt.hashpw(bytes, salt)

    return hash
    #for testing, store in global array
    #global stored_hash = {}

def check_password(input):
    hash = password_hash(input)

    result = bcrypt.checkpw(bytes,hash)

    return result