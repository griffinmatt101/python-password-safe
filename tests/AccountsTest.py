from unittest import TestCase
from unittest import mock as MOCK
from unittest.mock import patch

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


hashMock = HashClass()
hashMock.pwd = 'pwd'
hashMock.salt = 'salt'

class TestAccount(TestCase):

    '''
    addAccount tests
    '''
    @patch('Hash.HashClass.newPasswordHash')
    @patch('db.Database.PasswordDatabase.addUser')
    def testAddAccountSuccess(self, mockUser, mockHash):

        testAccounts = UserAccount('','')
        testStr = ''

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

    @patch('Hash.HashClass.newPasswordHash')
    @patch('db.Database.PasswordDatabase.addUser', side_effect=UserExistsException())
    def testAddAccountUserExists(self, mockUser, mockHash):

        testAccounts = UserAccount('','')
        testStr = 'Username already exists!\n'

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

    @patch('Hash.HashClass.newPasswordHash')
    @patch('db.Database.PasswordDatabase.addUser', side_effect=DatabaseErrorException('DB ERROR'))
    def testAddAccountDatabaseError(self, mockUser, mockHash):

        testAccounts = UserAccount('','')
        testStr = 'Database error\n'

        with MOCK.patch('sys.stdout', new=io.StringIO()) as fake_str:
            testAccounts.addAccount()

        self.assertEqual(fake_str.getvalue(),testStr)

    '''
    selectAccount tests
    '''
    @patch('db.Database.PasswordDatabase.selectUser', side_effect=UserDoesNotExistException())
    def testSelectAccountUserDoesNotExist(self, mockUser):

        testAccounts = UserAccount('test','test')

        self.assertEqual(testAccounts.selectAccount(),None)

    @patch('db.Database.PasswordDatabase.selectUser', side_effect=DatabaseErrorException('DB ERROR'))
    def testSelectAccountDatabaseError(self, mockUser):

        testAccounts = UserAccount('test','test')

        self.assertEqual(testAccounts.selectAccount(),None)

    
    @patch('db.Database.PasswordDatabase.selectUser', return_value = hashMock)
    def testSelectAccount(self, mockUser):

        testAccounts = UserAccount('test','test')

        self.assertEqual(testAccounts.selectAccount(), hashMock)

    '''
    checkAuth tests
    '''
    def testCheckAuthIsAuthTrue(self):

        testAccounts = UserAccount('test', 'test')
        testAccounts.isAuth = True

        self.assertTrue(testAccounts.checkAuth(hashMock))

    @patch('Hash.HashClass.checkHashWithSalt', return_value = False)
    def testCheckAuthHashFalse(self, mockUser):

        testAccounts = UserAccount('test', 'test')
        
        self.assertFalse(testAccounts.checkAuth(hashMock))

    @patch('Hash.HashClass.checkHashWithSalt', return_value = True)
    def testCheckAuthHashTrue(self, mockUser):

        testAccounts = UserAccount('test', 'test')

        self.assertTrue(testAccounts.checkAuth(hashMock))
