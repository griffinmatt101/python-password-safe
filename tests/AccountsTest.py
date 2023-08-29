from unittest import TestCase
from unittest import mock as MOCK
from unittest.mock import patch
from mockito import when, mock

import sys
import os
import io
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from Accounts import UserAccount
from db.Database import PasswordDatabase
from exceptions.Exceptions import UserExistsException
from exceptions.Exceptions import DatabaseErrorException
from Hash import HashClass


class TestAddAccount(TestCase):


    def testAddAccountDatabaseError(self):

        instance = mock(PasswordDatabase)
        testAccounts = UserAccount('','')
        testStr = 'Database error\n'

        #when(instance).addUser(any,any).thenRaise(DatabaseErrorException)

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            with when(instance).addUser(...).thenRaise(UserExistsException):
                testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)


    def testAddAccountUserExists(self):

        instance = mock(PasswordDatabase)
        testAccounts = UserAccount('matt_test_1','test_pass_1')
        testStr = 'Username already exists!\n'

        # when addUser function from PasswordDatabase class is called,
        # raise UserExistsException
        # when(instance).addUser(...).thenRaise(UserExistsException)

        # test output string matches
        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            with when(instance).addUser(...).thenRaise(UserExistsException):
                testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

    # if __name__ == '__main__':
    #     unittest.main()