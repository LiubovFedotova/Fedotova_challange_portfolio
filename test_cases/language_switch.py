import os
import time
import unittest

from selenium import webdriver

from pages.addplayer_page import AddPlayer
from pages.dashboard import Dashboard
from pages.editplayer_page import EditPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLanguageSwitch(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_language_switch(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(4)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_language_button()
        dashboard_page.check_language_is_switched()

    @classmethod
    def tearDown(self):
        self.driver.quit()