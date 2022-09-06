import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class EditPlayer(BasePage):
    edit_page_url = 'https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/edit'
    expected_title_xpath = "//main/div[2]/form/div[1]/div/span"
    expected_title = 'Edit player Test Test'

    def title_of_edit_page(self):
        self.wait_url_changes('https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/edit')
        assert self.get_page_title(self.edit_page_url) == self.expected_title






