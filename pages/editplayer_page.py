import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class EditPlayer(BasePage):
    edit_page_url = 'https://scouts.futbolkolektyw.pl/players/631aea0354a32e8fe5dd9265/edit'
    expected_title_xpath = "//main/div[2]/form/div[1]/div/span"
    expected_title = 'Edit player Test Test'

    def title_of_edit_page(self):
        self.wait_url_changes('https://scouts.futbolkolektyw.pl/players/631aea0354a32e8fe5dd9265/edit')
        assert self.get_page_title(self.edit_page_url) == self.expected_title






