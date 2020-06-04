import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from custom_wait import presence_of_elements
from pages.locators import DashboardPageLocators, LoginPageLocators, HeaderLocators


class OxwallHelper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)

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

    def wait_signin(self):
        sign_in1 = self.wait.until(expected_conditions.element_to_be_clickable(
            HeaderLocators.SIGN_IN_BUTTON)
        )
        sign_in1.click()

    #  log in - end
    #  COMPLETE YOUR PROFILE - start

    # def radio_gender_male(self):
    #     wait = WebDriverWait(self.driver, 15)
    #     radio = wait.until(expected_conditions.element_to_be_clickable(
    #         (By.XPATH, '//ul[@class="ow_radio_group clearfix"]/li/input[@value="1"]'))
    #     )
    #     # wait.until(expected_conditions.visibility_of_element_located(
    #     #     (By.XPATH, '//div[text()="You need to enter required values."]'))
    #     # )
    #     wait.until(expected_conditions.invisibility_of_element(
    #         (By.XPATH, '//div[text()="You need to enter required values."]'))
    #     )
    #     radio.click()
    #
    # def birthdate_input(self):
    #     combobox_day = self.driver.find_element(By.NAME, "day_birthdate")
    #     dropdown1 = Select(combobox_day)
    #     dropdown1.select_by_visible_text('24')
    #     combobox_month = self.driver.find_element(By.NAME, "month_birthdate")
    #     dropdown2 = Select(combobox_month)
    #     dropdown2.select_by_visible_text('Apr')
    #     combobox_year = self.driver.find_element(By.NAME, "year_birthdate")
    #     dropdown3 = Select(combobox_year)
    #     dropdown3.select_by_visible_text('1981')
    #
    # def submit(self):
    #     submit = self.driver.find_element(By.XPATH, '//input[@name="submit"]')
    #     submit.click()

    #  COMPLETE YOUR PROFILE - end
    #  post message - start

    def post_message(self, message):
        textfield = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.NAME, 'status'))
        )
        textfield.send_keys(message)
        post = self.driver.find_element(By.NAME, 'save')
        post.click()

    def wait_new_post_appear(self, count_posts_before):
        return self.wait.until(presence_of_elements(*DashboardPageLocators.POST_TEXT, count_posts_before + 1),
                               message="less than")

    #  post message - end
    #  comment - start

    def post_comment(self, text):
        comment_buttons = self.driver.find_elements(By.XPATH,
                                                    '//span[@class="ow_miniic_comment newsfeed_comment_btn "]')
        comment_buttons[0].click()
        comment_text_field = self.driver.find_elements(By.XPATH, '//textarea[@class="comments_fake_autoclick"]')
        comment_text_field[0].send_keys(text)
        comment_text_field[0].send_keys(Keys.ENTER)

    def wait_new_comment_appear(self, count_comments_before):
        return self.wait.until(presence_of_elements((By.XPATH, '//div[@class="ow_comments_content ow_smallmargin"]'),
                                                    count_comments_before + 1), message="less than")

    #  comment - end
    #  signup - start

    def click_signup_button(self):
        signup_button = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[text()="Sign up"]'))
        )
        signup_button.click()

    def input_username_email_password(self, username, email1, password1):
        user_name = self.wait.until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, '//input[@class="ow_username_validator" and contains (@type, text)]'))
        )
        user_name[0].send_keys(username)
        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys(email1)
        password = self.wait.until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, '//input[@name="password" and contains (@type, password)]'))
        )
        password[0].send_keys(password1)
        password_repeat = self.driver.find_element(By.XPATH,
                                                   '//input[@name="repeatPassword" and contains (@type, password)]')
        password_repeat.send_keys(password1)
        real_name = self.wait.until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, '//input[@type="text"]'))
        )
        real_name[-1].send_keys(username)

    def press_male_radiobutton(self):
        male_radio = self.wait.until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, '//input[@type="radio" and contains (@value, "1")]'))
        )
        male_radio[0].click()

    def select_day_month_year(self, day, month, year):
        combo_list = self.wait.until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, '//div[@class="ow_inline owm_inline"]/select[@type="text"]'))
        )
        dropdown_day = Select(combo_list[0])
        dropdown_day.select_by_visible_text(day)
        dropdown_month = Select(combo_list[1])
        dropdown_month.select_by_visible_text(month)
        dropdown_year = Select(combo_list[2])
        dropdown_year.select_by_visible_text(year)

    def check_male_fun(self):
        checkbox_male = self.wait.until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, '//ul[@class="ow_checkbox_group clearfix"]/li/label[text()="Male"]'))
        )
        checkbox_male[0].click()
        checkbox_fun = self.wait.until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, '//ul[@class="ow_checkbox_group clearfix"]/li/label[text()="Fun"]'))
        )
        checkbox_fun[0].click()

    def fill_in_textareas(self, music, books):
        textarea_list = self.wait.until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, '//textarea'))
        )
        music_area = textarea_list[0]
        favorite_books_area = textarea_list[1]
        music_area.send_keys(music)
        favorite_books_area.send_keys(books)

    def upload_photo(self):
        user_photo_block = self.driver.find_element(By.XPATH, '//input[@name="userPhoto" and contains (@type, "file")]')
        user_photo_block.send_keys(os.getcwd() + '\MyPhoto.jpg')
        apply_crop = self.wait.until(expected_conditions.element_to_be_clickable((By.ID, 'avatar-crop-btn')))
        apply_crop.click()

    def submit(self):
        join_button2 = self.wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'joinSubmit')))
        scroll = (
            ActionChains(self.driver)
                .move_to_element(join_button2)
                .click(join_button2)
                .perform()
        )

    #  signup - end
