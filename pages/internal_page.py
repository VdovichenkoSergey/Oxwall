from pages.base_page import Page
from pages.locators import HeaderLocators


class InternalPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

        # self.sign_in_menu = self.find_element(HeaderLocators.SIGN_IN_BUTTON)
        # self.sign_up_menu = self.find_element(HeaderLocators.SIGN_UP_BUTTON)
        #
        # self.main_menu = self.find_element(HeaderLocators.MAIN_MENU)
        # self.join_menu = self.find_element(HeaderLocators.JOIN_MENU)

    @property
    def sign_in_menu(self):
        return self.driver.find_element(*HeaderLocators.SIGN_IN_BUTTON)

    def click_sign_in(self):
        self.sign_in_menu.click()


class MainPage(InternalPage):
    pass


class LoginPage(Page):
    pass
