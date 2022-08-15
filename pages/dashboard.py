from pages.base_page import BasePage


class Dashboard(BasePage):
    players_count_block_xpath = "//div[1]/div[contains(@class,'MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded')]"
    matches_count_block_xpath = "//div[2]/div[contains(@class,'MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded')]"
    reports_count_block_xpath = "//div[3]/div[contains(@class,'MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded')]"
    events_count_block_xpath = "//div[4]/div[contains(@class,'MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded')]"
    scouts_panel_block_xpath = "//*/div[1]/div/div[2]/h2"
    dev_team_contact_button_xpath = "///*/div[1]/div/div[3]/a"
    shortcuts_block_xpath = "//*/div[2]/div/div/h2"
    add_players_button_xpath = "//*/div[2]/div/div/a"
    activity_block_xpath = "//*/div[3]/div/div/h2"
    super_man_button_xpath = "//*/div[3]/div/div/a"
    main_page_link_xpath = "//*[contains(@class,'MuiListItemText-root jss58 jss59')]"
    main_page_icon_xpath = "//*[contains(@class,'MuiSvgIcon-root jss58 jss59')]"
    players_page_link_xpath = "//*[contains(@class,'MuiListItemText-root jss58 jss60')]"
    players_page_icon_xpath = "//*[contains(@class,'MuiSvgIcon-root jss58 jss163')]"
    language_selection_xpath = "//*/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*/ul[2]/div[2]/div[2]/span"


