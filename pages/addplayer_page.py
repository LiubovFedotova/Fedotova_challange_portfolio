from pages.base_page import BasePage


class AddPlayer(BasePage):
    name_field_xpath = "// *[@name='name']"
    surname_field_xpath = "// *[@name='surname']"
    age_field_xpath = "// *[@name='age']"
    mainPosition_field_xpath = "// *[@name='mainPosition']"
    submit_button_xpath = "// *[text()= 'Submit']"
    new_player_button_xpath = "//ul[2]/div[1]"
    clear_button_xpath = "// *[text()= 'Clear']"
    expected_title_of_add_page = 'Add player'
    add_page_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'


    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_mainPosition(self, mainPosition):
        self.field_send_keys(self.mainPosition_field_xpath, mainPosition)

    def click_on_the_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)
        self.wait_url_changes('https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/edit')

    def click_on_the_clear_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.clear_button_xpath)

    def title_of_add_page(self):
        assert self.get_page_title(self.add_page_url) == self.expected_title_of_add_page







