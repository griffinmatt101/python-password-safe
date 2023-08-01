'''
Thrown when an unknown database error is encountered
'''
class DatabaseErrorException(Exception):

    def __init__(self, message):
        self.message = message

'''
Thrown when database returns an Integrity error when checking unique username
'''
class UserExistsException(Exception):

    def __init__(self):
        pass

'''
Thrown when database returns Programming error (Undefined Column)
'''
class UserDoesNotExistException(Exception):

    def __init__(self):
        pass