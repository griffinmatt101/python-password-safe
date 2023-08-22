from unittest import TestCase
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from Accounts import UserAccount

class TestAddAccount(TestCase):

    def testAddAccountUserExists(self):
        testAccounts = UserAccount('matt_test_1','test_pass_1')
        testStr = 'Username already exists!'

        with patch.object(PasswordDatabase, 'doesUserExistDB', return_value=True):
            self.assertEqual(testAccounts.addAccount(),testStr)

    # if __name__ == '__main__':
    #     unittest.main()