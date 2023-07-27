# Method to create a new password hash

import bcrypt

def password_hash(input):
    #convert password to array of bytes
    bytes = input.encode('utf-8')

    #generate salt
    salt = bcrypt.gensalt()

    #hash password
    hash = bcrypt.hashpw(bytes, salt)

    #for testing, output hash
    print(hash)