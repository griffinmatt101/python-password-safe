from unittest import TestCase
from unittest.mock import patch, call
from mockito import mock, when

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from Accounts import UserAccount
from db.Database import PasswordDatabase
from exceptions.Exceptions import UserExistsException
from Hash import HashClass


class TestAddAccount(TestCase):

    @patch('builtins.print')
    def testAddAccountUserExists(self):
        instance = PasswordDatabase()
        testAccounts = UserAccount('matt_test_1','test_pass_1')
        testStr = 'Username already exists!'

        # when addUser function from PasswordDatabase class is called,
        # return UserExistsException
        when(instance).addUser(...).thenRaise(UserExistsException)
        output = testAccounts.addAccount()
        assert output == call(testStr)
        #self.assertEqual(testAccounts.addAccount(),testStr)

    # if __name__ == '__main__':
    #     unittest.main()