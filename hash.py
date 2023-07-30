import accounts

class Hash(UserAccount):
    
    def __init__(self,pwd):
        self.pwd = pwd
        #don't create salt until we pull from db
        self.salt = None
        #bcrypt.gensalt()

    # Need to store each individual salt in DB and use it when checking
    # Method to create a new password hash
    def password_hash(self):
        #convert password to array of bytes
        bytes = pwd.encode('utf-8')

        #first check if user is in DB
        #if so, pull salt from db and set it here
        #if not, create new salt, add it to DB
        hash = bcrypt.hashpw(bytes, self.salt)

        return hash

    def check_password(self,pwd, check_val):
        hash = password_hash(pwd)

        result = bcrypt.checkpw(check_val,hash)

        return result