import bcrypt

class HashClass:
    
    def __init__(self):
        self.pwd = None
        self.salt = None

    def passwordHashWithSalt(self):
        bytes = self.pwd.encode('utf-8')
        
        return

    '''
    Create a new password hash and sets the salt
    '''
    def newPasswordHash(self,pwd):

        bytes = pwd.encode('utf-8')
        self.salt = bcrypt.gensalt()
        self.pwd = bcrypt.hashpw(bytes, self.salt)

    def doesPasswordMatch(self,pwd, check_val):
        hash = passwordHash(pwd)

        result = bcrypt.checkpw(check_val,hash)

        return result