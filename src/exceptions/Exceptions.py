
'''
Thrown when database returns an Integrity error when checking unique username
'''
class UserExistsException(Exception):

    def __init__(self):
        pass