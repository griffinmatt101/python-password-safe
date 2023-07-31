
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