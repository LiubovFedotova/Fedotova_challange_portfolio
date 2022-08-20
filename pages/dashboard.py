import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    players_count_block_xpath = "//*/div[2]/div[1]/div"
    matches_count_block_xpath = "//*/div[2]/div[2]/div"
    reports_count_block_xpath = "//*/div[2]/div[3]/div"
    events_count_block_xpath = "//*/div[2]/div[4]/div"
    scouts_panel_block_xpath = "//*/div[1]/div/div[2]/h2"
    dev_team_contact_button_xpath = "///*/div[1]/div/div[3]/a"
    shortcuts_block_xpath = "//*/div[2]/div/div/h2"
    add_players_button_xpath = "//*/div[2]/div/div/a"
    activity_block_xpath = "//*/div[3]/div/div/h2"
    super_man_button_xpath = "//*/div[3]/div/div/a"
    main_page_link_xpath = "//*/ul[1]/div[1]/div[2]"
    main_page_icon_xpath = "//*[contains(@class,'MuiListItemText-root jss29 jss30')]"
    players_page_link_xpath = "//*[contains(@class,'MuiSvgIcon-root jss29 jss30')]"
    players_page_icon_xpath = "//*[contains(@class,'MuiSvgIcon-root jss29 jss134')]"
    language_selection_xpath = "//*/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*/ul[2]/div[2]/div[2]/span"
