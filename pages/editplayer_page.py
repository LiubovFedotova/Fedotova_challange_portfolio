import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class EditPlayer(BasePage):
    edit_page_url = 'https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/edit'
    expected_title_xpath = "//main/div[2]/form/div[1]/div/span"
    expected_title = 'Edit player Test Test'
    added_player_message_xpath = "//*[text()= 'Added player.']"
    text_of_added_player_message = 'Added player.'
    redirect_massage_xpath = "//*[text()= 'Redirect to edit page']"
    text_of_redirect_massage = 'Redirect to edit page'

    def title_of_edit_page(self):
        self.wait_url_changes('https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/edit')
        assert self.get_page_title(self.edit_page_url) == self.expected_title

    def check_validation_message_add(self):
        self.wait_for_element_to_be_clickable(self. expected_title_xpath)
        self.assert_element_text(self.added_player_message_xpath, self.text_of_added_player_message)

    def check_validation_message_redirect(self):
        self.wait_for_element_to_be_clickable(self. expected_title_xpath)
        self.assert_element_text(self.redirect_massage_xpath, self.text_of_redirect_massage)




