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
        bytes = pwd.encode('utf-8')

        # "Unicode-objects must be encoded before hashing"
        try:
            pwdTry = bcrypt.hashpw(bytes,self.salt)

            if(pwdTry == self.pwd):
                print('true')
            else:
                print('false')

        except Exception as e:
            print(e)
        
        # result = bcrypt.checkpw(pwd,self.pwd)
        # print(result)

        return True 

    '''
    Create a new password hash and sets the salt
    '''
    def newPasswordHash(self,pwd):

        bytes = pwd.encode('utf-8')
        self.salt = bcrypt.gensalt()
        self.pwd = bcrypt.hashpw(bytes, self.salt)