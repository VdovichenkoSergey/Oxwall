import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def test_login(oxwall, driver):
    oxwall.wait_signin()
    oxwall.sign_in(login='admin', password='pass')
    wait = WebDriverWait(driver, 5)
    welcome = wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//div[@class="ow_box_cap_body"]/h3[@class="ow_ic_info"]'))
    )

    assert welcome.is_displayed() == True


def test_create_messages(oxwall, driver, loged_user, message_list):
    oxwall.post_message(message_list)
    all_posts = driver.find_elements(By.XPATH, '//div[@class="ow_newsfeed_content ow_smallmargin"]')
    oxwall.wait_new_post_appear(len(all_posts))
    all_posts2 = driver.find_elements(By.XPATH, '//div[@class="ow_newsfeed_content ow_smallmargin"]')
    users = driver.find_elements(By.XPATH, '//div[@class="ow_newsfeed_string ow_small ow_smallmargin"]/a/b')

    assert all_posts2[0].text == message_list
    assert users[0].text == loged_user.capitalize()


def test_create_comments(oxwall, driver, loged_user):
    oxwall.post_message('Comments creating - test!!!')
    all_posts = driver.find_elements(By.XPATH, '//div[@class="ow_newsfeed_content ow_smallmargin"]')
    oxwall.wait_new_post_appear(len(all_posts))
    comment = 'New comment!!!'
    oxwall.post_comment(comment)
    post_list = driver.find_elements(By.XPATH, '//div[@class="ow_comments_content ow_smallmargin"]')
    oxwall.wait_new_comment_appear(len(post_list))
    post_list2 = driver.find_elements(By.XPATH, '//div[@class="ow_comments_content ow_smallmargin"]')

    assert post_list2[0].text == comment


def test_delete_message(oxwall, driver, loged_user):
    time.sleep(2)
    menu_button = driver.find_elements(By.XPATH, '//div[@class="ow_newsfeed_context_menu"]')
    action_chain = (
        ActionChains(driver)
            .move_to_element(menu_button[-1])
            .pause(2)
            .click(menu_button[-1])
            .perform()
    )
    delete_button = driver.find_elements(By.XPATH, '//a[@class="newsfeed_remove_btn owm_red_btn"]')
    delete_button[-1].click()
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    assert menu_button[-1].is_displayed() == False


def test_signup(oxwall, driver, wait):
    oxwall.click_signup_button()
    oxwall.input_username_email_password('Testuser8', 'test8@test.com', 'q123456_')
    oxwall.press_male_radiobutton()
    oxwall.select_day_month_year('24', 'Apr', '1981')
    oxwall.check_male_fun()
    oxwall.fill_in_textareas(music='rock and some another heavy music', books='fantasy')
    oxwall.upload_photo()
    oxwall.submit()

    welcome = wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//div[@class="ow_box_cap_body"]/h3[@class="ow_ic_info"]'))
    )

    assert welcome.is_displayed() == True



















