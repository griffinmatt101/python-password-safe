import bcrypt

# Method to create a new password hash
# !!! Change this! Separate the hash function to it's own func
def password_hash(name,pwd):
    #convert password to array of bytes
    bytes = pwd.encode('utf-8')

    #generate salt
    salt = bcrypt.gensalt()

    #hash password
    hash = bcrypt.hashpw(bytes, salt)

    #for testing, store in global array
    global stored_hash = {name:hash}

def check_password(input):
    bytes = input.encode('utf-8')

    result = bcrypt.checkpw(bytes,stored_hash)

    return result