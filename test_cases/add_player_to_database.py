import os
import time
import unittest

from selenium import webdriver

from pages.addplayer_page import AddPlayer
from pages.dashboard import Dashboard
from pages.editplayer_page import EditPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
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
        addplayer_page.type_in_email('test@gmail.com')
        addplayer_page.type_in_name('Test')
        addplayer_page.type_in_surname('Test')
        addplayer_page.type_in_phone('111111111')
        addplayer_page.type_in_weight('100')
        addplayer_page.type_in_height('190')
        addplayer_page.type_in_age('01.01.2001')
        addplayer_page.click_on_leg()
        addplayer_page.type_in_club('test')
        addplayer_page.type_in_level('test')
        addplayer_page.type_in_mainPosition('test')
        addplayer_page.type_in_secondPosition('test')
        addplayer_page.click_on_district()
        addplayer_page.type_in_achievements('test')
        addplayer_page.type_in_laczy_nas_pilka('test')
        addplayer_page.type_in_ninety_minut('test')
        addplayer_page.type_in_facebook('test')
        addplayer_page.click_on_the_submit_button()
        editplayer_page = EditPlayer(self.driver)
        editplayer_page.title_of_edit_page()


    @classmethod
    def tearDown(self):
        self.driver.quit()