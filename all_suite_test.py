import unittest

from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.add_player_to_database import TestAddPlayer
from test_cases.clear_add_player_form import TestClearAddPlayerForm
from test_cases.invalid_login_to_the_system import TestInvalidPassword
from test_cases.language_switch import TestLanguageSwitch
from test_cases.Log_out_of_the_system import TestLogout


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(Test))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestLogout))
   test_suite.addTest(makeSuite(TestInvalidPassword))
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestClearAddPlayerForm))
   test_suite.addTest(makeSuite(TestLanguageSwitch))
   return test_suite




if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())