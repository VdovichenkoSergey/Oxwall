import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from custom_wait import presence_of_elements


class OxwallHelper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)

    # def switch_to_frame(self):
    #     frame1 = self.driver.find_element(By.NAME, 'demobody')
    #     self.driver.switch_to.frame(frame1)

    #  log in - start

    def sign_in(self, login, password):
        username = self.driver.find_element(By.NAME, "identity")
        password1 = self.driver.find_element(By.NAME, "password")
        sign = self.driver.find_element(By.NAME, "submit")
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
        wait = WebDriverWait(self.driver, 15)
        sign_in1 = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//span[@class="ow_signin_label"]'))
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
        wait = WebDriverWait(self.driver, 15)
        textfield = wait.until(expected_conditions.element_to_be_clickable(
            (By.NAME, 'status'))
        )
        textfield.send_keys(message)
        post = self.driver.find_element(By.NAME, 'save')
        post.click()

    def wait_new_post_appear(self, count_posts_before):
        return self.wait.until(presence_of_elements((By.CSS_SELECTOR, ".ow_newsfeed_content"), count_posts_before + 1),
                               message="less than")

    #  post message - end

    def post_comment(self, text):
        comment_buttons = self.driver.find_elements(By.XPATH, '//span[@class="ow_miniic_comment newsfeed_comment_btn "]')
        comment_buttons[0].click()
        comment_text_field = self.driver.find_elements(By.XPATH, '//textarea[@class="comments_fake_autoclick"]')
        comment_text_field[0].send_keys(text)
        comment_text_field[0].send_keys(Keys.ENTER)

    def wait_new_comment_appear(self, count_comments_before):
        return self.wait.until(presence_of_elements((By.XPATH, '//div[@class="ow_comments_content ow_smallmargin"]'),
                                                    count_comments_before + 1), message="less than")