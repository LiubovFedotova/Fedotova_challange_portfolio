import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):

    players_count_block_xpath = "//*/div[2]/div[1]/div"
    matches_count_block_xpath = "//*/div[2]/div[2]/div"
    reports_count_block_xpath = "//*/div[2]/div[3]/div"
    events_count_block_xpath = "//*/div[2]/div[4]/div"
    scouts_panel_block_xpath = "//*/div[1]/div/div[2]/h2"
    dev_team_contact_button_xpath = "///*/div[1]/div/div[3]/a"
    shortcuts_block_xpath = "//*/div[2]/div/div/h2"
    add_players_button_xpath = "//*/div[2]/div/div/a"
    activity_block_xpath = "//*/div[3]/div/div/h2"
    futbol_kolektyw_button_xpath = "//*[@title = 'Logo Scouts Panel']"
    main_page_link_xpath = "//*/ul[1]/div[1]/div[2]"
    main_page_icon_xpath = "//*[contains(@class,'MuiListItemText-root jss29 jss30')]"
    players_page_link_xpath = "//*[contains(@class,'MuiSvgIcon-root jss29 jss30')]"
    players_page_icon_xpath = "//*[contains(@class,'MuiSvgIcon-root jss29 jss134')]"
    language_button_xpath = "//*/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*[text()= 'Sign out']"

    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_players_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_sign_out_button(self):
        self.wait_for_element_to_be_clickable(self.sign_out_button_xpath)
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_on_the_add_player_button(self):
        self.wait_for_element_to_be_clickable(self.add_players_button_xpath)
        self.click_on_the_element(self.add_players_button_xpath)

    def click_on_the_language_button(self):
        self.wait_for_element_to_be_clickable(self.add_players_button_xpath)
        self.click_on_the_element(self.language_button_xpath)




    pass
