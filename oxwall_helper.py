import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from custom_wait import presence_of_elements
from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.main_page import MainPage
from pages.locators import DashboardPageLocators, LoginPageLocators, HeaderLocators, PostLocators, JoinLocators


class OxwallHelper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)
        self.main_page = MainPage(driver)
        self.dashboard_page = DashboardPage(driver)

    # def switch_to_frame(self):
    #     frame1 = self.driver.find_element(By.NAME, 'demobody')
    #     self.driver.switch_to.frame(frame1)

    #  log in - start

    def sign_in(self, login, password):
        username = self.driver.find_element(*LoginPageLocators.USERNAME_FIELD)
        password1 = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        sign = self.driver.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        action = (
            ActionChains(self.driver)
                .move_to_element(username)
                .click(username)
                .send_keys(login)
                .move_to_element(password1)
                .click(password1)
                .send_keys(password)
                .click(sign)
                .perform()
        )
        welcome = self.wait.until(expected_conditions.visibility_of_element_located(DashboardPageLocators.LOGIN_CONFIRM)
                             )
        return welcome

    def wait_signin(self):
        sign_in1 = self.wait.until(expected_conditions.element_to_be_clickable(
            HeaderLocators.SIGN_IN_BUTTON)
        )
        sign_in1.click()

    def post_message(self, message):
        textfield = self.wait.until(expected_conditions.element_to_be_clickable(PostLocators.TEXT_AREA_FOR_POST))
        textfield.send_keys(message)
        post = self.driver.find_element(By.NAME, 'save')
        post.click()

    def wait_new_post_appear(self, count_posts_before):
        return self.wait.until(presence_of_elements(DashboardPageLocators.POST_TEXT, count_posts_before + 1),
                               message="less than")

    def press_menu_button_in_post(self):
        post_blocks = self.driver.find_elements(*DashboardPageLocators.LIST_OF_POST_BLOCKS)
        menu_button = self.driver.find_elements(*PostLocators.MENU_BUTTON_LIST)
        action_chain = (
            ActionChains(self.driver)
                .move_to_element(post_blocks[-1])
                .move_to_element(menu_button[-1])
                .perform()
        )
        return post_blocks

    def press_delete_button(self):
        delete_button = self.driver.find_elements(*PostLocators.DELETE_BUTTON_LIST)
        delete_button[-1].click()

    def confirm_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    #  post message - end
    #  comment - start

    def post_comment(self, text):
        comment_buttons = self.driver.find_elements(*PostLocators.COMMENT_BUTTON_LIST)
        comment_buttons[0].click()
        comment_text_field = self.driver.find_elements(*PostLocators.COMMENT_TEXT_FIELD_LIST)
        comment_text_field[0].send_keys(text)
        comment_text_field[0].send_keys(Keys.ENTER)

    def wait_new_comment_appear(self, count_comments_before):
        return self.wait.until(presence_of_elements(DashboardPageLocators.LIST_OF_COMMENTS,
                                                    count_comments_before + 1), message="less than")

    #  comment - end
    #  signup - start

    def click_signup_button(self):
        signup_button = self.wait.until(expected_conditions.element_to_be_clickable(HeaderLocators.SIGN_UP_BUTTON))
        signup_button.click()

    def input_username_email_password(self, username, email1, password1):
        user_name = self.wait.until(expected_conditions.visibility_of_any_elements_located(JoinLocators.USER_NAME_FIELD))
        user_name[0].send_keys(username)
        email = self.driver.find_element(*JoinLocators.EMAIL_FIELD)
        email.send_keys(email1)
        password = self.wait.until(expected_conditions.visibility_of_any_elements_located(JoinLocators.PASSWORD_FIELD))
        password[0].send_keys(password1)
        password_repeat = self.driver.find_element(*JoinLocators.PASSWORD_REPEAT_FIELD)
        password_repeat.send_keys(password1)
        real_name = self.wait.until(expected_conditions.visibility_of_any_elements_located(JoinLocators.REAL_NAME_FIELD))
        real_name[-1].send_keys(username)

    def press_male_radiobutton(self):
        male_radio = self.wait.until(expected_conditions.visibility_of_any_elements_located(JoinLocators.MALE_RADIO))
        male_radio[0].click()

    def select_day_month_year(self, day, month, year):
        combo_list = self.wait.until(expected_conditions.visibility_of_any_elements_located(JoinLocators.BIRTH_COMBO_LIST))
        dropdown_day = Select(combo_list[0])
        dropdown_day.select_by_visible_text(day)
        dropdown_month = Select(combo_list[1])
        dropdown_month.select_by_visible_text(month)
        dropdown_year = Select(combo_list[2])
        dropdown_year.select_by_visible_text(year)

    def check_male_fun(self):
        checkbox_male = self.wait.until(expected_conditions.visibility_of_any_elements_located(JoinLocators.MALE_CHECKBOX))
        checkbox_male[0].click()
        checkbox_fun = self.wait.until(expected_conditions.visibility_of_any_elements_located(JoinLocators.FUN_CHECKBOX))
        checkbox_fun[0].click()

    def fill_in_textareas(self, music, books):
        textarea_list = self.wait.until(expected_conditions.visibility_of_any_elements_located(JoinLocators.TEXTAREA_LIST))
        music_area = textarea_list[0]
        favorite_books_area = textarea_list[1]
        music_area.send_keys(music)
        favorite_books_area.send_keys(books)

    def upload_photo(self):
        user_photo_block = self.driver.find_element(*JoinLocators.PHOTO_BLOCK)
        user_photo_block.send_keys(os.getcwd() + '\MyPhoto.jpg')
        apply_crop = self.wait.until(expected_conditions.element_to_be_clickable(JoinLocators.APPLY_CROP_BUTTON))
        apply_crop.click()

    def submit(self):
        join_button2 = self.wait.until(expected_conditions.element_to_be_clickable(JoinLocators.JOIN_BUTTON))
        scroll = (
            ActionChains(self.driver)
                .move_to_element(join_button2)
                .click(join_button2)
                .perform()
        )

    #  signup - end
