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
from exceptions.Exceptions import UserDoesNotExistException
from exceptions.Exceptions import DatabaseErrorException
from Hash import HashClass


class TestAddAccount(TestCase):

    '''
    addAccount tests
    '''
    @patch('db.Database.PasswordDatabase.addUser')
    def testAddAccountSuccess(self,mockUser):

        testAccounts = UserAccount('','')
        testStr = ''

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

    @patch('db.Database.PasswordDatabase.addUser', side_effect=UserExistsException())
    def testAddAccountUserExists(self,mockUser):

        testAccounts = UserAccount('','')
        testStr = 'Username already exists!\n'

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

    @patch('db.Database.PasswordDatabase.addUser', side_effect=DatabaseErrorException('DB ERROR'))
    def testAddAccountDatabaseError(self,mockUser):

        testAccounts = UserAccount('','')
        testStr = 'Database error\n'

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

    '''
    checkAuth tests
    '''
    @patch('db.Database.PasswordDatabase.selectUser', side_effect=UserDoesNotExistException())
    def testCheckAuthUserDoesNotExist(self,mockUser):

        testAccounts = UserAccount('test','test')
        testStr = 'Username %s does not exist! \n' % testAccounts.uname

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.checkAuth()

        self.assertEqual(fake_str.getvalue(),testStr)

    @patch('db.Database.PasswordDatabase.selectUser', side_effect=DatabaseErrorException('DB ERROR'))
    def testCheckAuthDatabaseError(self,mockUser):

        testAccounts = UserAccount('test','test')
        testStr = 'Database Error\n'

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.checkAuth()

        self.assertEqual(fake_str.getvalue(),testStr)

