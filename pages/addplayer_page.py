import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    phone_field_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@name='weight']"
    height_field_xpath = "//*[@name='height']"
    age_field_xpath = "//*[@name='age']"
    leg_dropdown_field_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_field_xpath = "//ul/li[1]"
    club_field_xpath = "//*[@name='club']"
    level_field_xpath = "//*[@name='level']"
    mainPosition_field_xpath = "//*[@name='mainPosition']"
    secondPosition_field_xpath = "//*[@name='secondPosition']"
    district_dropdown_field_xpath = "//*[@id='mui-component-select-district']"
    lublin_district_field_xpath = "//ul/li[3]"
    achievements_field_xpath = "//*[@name='achievements']"
    laczy_nas_pilka_field_xpath = "//*[@name='webLaczy']"
    ninety_minut_field_xpath = "//*[@name='web90']"
    facebook_field_xpath = "//*[@name='webFB']"
    submit_button_xpath = "//*[text()= 'Submit']"
    new_player_button_xpath = "//ul[2]/div[1]"
    clear_button_xpath = "//*[text()= 'Clear']"

    expected_title_of_add_page = 'Add player'
    add_page_url = 'https://scouts.futbolkolektyw.pl/en/players/add'


    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)
    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)
    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)
    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)
    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)
    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)
    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)
    def click_on_leg(self):
        self.click_on_the_element(self.leg_dropdown_field_xpath)
        self.click_on_the_element(self.right_leg_field_xpath)
    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)
    def type_in_level(self, level):
        self.field_send_keys(self.club_field_xpath, level)
    def type_in_mainPosition(self, mainPosition):
        self.field_send_keys(self.mainPosition_field_xpath, mainPosition)
    def type_in_secondPosition(self, secondPosition):
        self.field_send_keys(self.secondPosition_field_xpath, secondPosition)
    def click_on_district(self):
        self.click_on_the_element(self.district_dropdown_field_xpath)
        self.click_on_the_element(self.lublin_district_field_xpath)
    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)
    def type_in_laczy_nas_pilka(self, webLaczy):
        self.field_send_keys(self.laczy_nas_pilka_field_xpath, webLaczy)
    def type_in_ninety_minut (self, ninety_minut):
        self.field_send_keys(self.ninety_minut_field_xpath, ninety_minut)
    def type_in_facebook (self, facebook):
        self.field_send_keys(self.facebook_field_xpath, facebook)
    def click_on_the_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)
    def click_on_the_clear_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.clear_button_xpath)
    def title_of_add_page(self):
        assert self.get_page_title(self.add_page_url) == self.expected_title_of_add_page







