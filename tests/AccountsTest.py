from unittest import TestCase
from unittest import mock as MOCK
from unittest.mock import patch
from mockito import when, mock, unstub, spy, verifyStubbedInvocationsAreUsed

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

    @patch('db.Database.PasswordDatabase.addUser', side_effect=UserExistsException())
    def testAddAccountUserExists(self,mockUser):

        testAccounts = UserAccount('','')
        testStr = 'Username already exists!\n'

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

    @patch('db.Database.PasswordDatabase.addUser', side_effect=DatabaseErrorException('Test'))
    def testAddAccountDatabaseError(self,mockUser):

        testAccounts = UserAccount('','')
        testStr = 'Database error\n'

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

