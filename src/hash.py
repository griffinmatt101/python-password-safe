import bcrypt

class HashClass:
    
    def __init__(self):
        self.pwd = None
        self.salt = None

    '''
    Compares password provided with password from database,
    using salt pulled from database
    '''
    def checkHashWithSalt(self,pwd):
        # encode to bytes
        pwdBytes = pwd.encode('utf-8')
        saltTest = self.salt.encode('utf-8')

        pwdTry = bcrypt.hashpw(pwdBytes,saltTest)

        if(pwdTry == self.pwd.encode('utf-8')):
            return True
        
        return False

    '''
    Create a new password hash and sets the salt
    '''
    def newPasswordHash(self,pwd):

        pwdBytes = pwd.encode('utf-8')
        self.salt = bcrypt.gensalt()
        self.pwd = bcrypt.hashpw(pwdBytes, self.salt).decode('utf-8')
        self.salt = self.salt.decode('utf-8')