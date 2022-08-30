import os
import time
import unittest

from selenium import webdriver

from pages.addplayer_page import AddPlayer
from pages.dashboard import Dashboard
from pages.editplayer_page import EditPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestClearAddPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_to_database(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        addplayer_page = AddPlayer(self.driver)
        addplayer_page.type_in_name('Test')
        addplayer_page.type_in_surname('Test')
        addplayer_page.type_in_age('01.01.2001')
        addplayer_page.type_in_mainPosition('test')
        addplayer_page.click_on_the_clear_button()


    @classmethod
    def tearDown(self):
        self.driver.quit()


