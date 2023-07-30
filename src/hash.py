import bcrypt

class HashClass:
    
    def __init__(self):
        self.pwd = None
        #don't create salt until we pull from db
        self.salt = None
        #bcrypt.gensalt()

    # Need to store each individual salt in DB and use it when checking
    # Method to create a new password hash
    def newPasswordHash(self,pwd):

        bytes = pwd.encode('utf-8')
        self.salt = bcrypt.gensalt()
        self.pwd = bcrypt.hashpw(bytes, self.salt)

    def doesPasswordMatch(self,pwd, check_val):
        hash = passwordHash(pwd)

        result = bcrypt.checkpw(check_val,hash)

        return result