import bcrypt

# Method to create a new password hash
# !!! Change this! Separate the hash function to it's own func
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