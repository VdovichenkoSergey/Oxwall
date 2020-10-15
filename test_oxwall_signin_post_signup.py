import time
from datetime import date

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import DashboardPageLocators
from value_objects.user import User


def test_login(oxwall, driver, wait):
    oxwall.wait_signin()
    welcome = oxwall.sign_in(login='admin', password='pass')

    assert welcome.is_displayed() == True


def test_create_messages(oxwall, driver, logged_user, message_list):
    oxwall.post_message(message_list)
    all_posts = driver.find_elements(*DashboardPageLocators.LIST_OF_ALL_POSTS)
    oxwall.wait_new_post_appear(len(all_posts))
    all_posts2 = driver.find_elements(*DashboardPageLocators.LIST_OF_ALL_POSTS)
    users = driver.find_elements(*DashboardPageLocators.LIST_OF_USERS_IN_POSTS)

    assert all_posts2[0].text == message_list
    assert users[0].text == logged_user.capitalize()


def test_create_comments(oxwall, driver, logged_user):
    oxwall.post_message('Comments creating - test!!!')
    all_posts = driver.find_elements(*DashboardPageLocators.LIST_OF_ALL_POSTS)
    oxwall.wait_new_post_appear(len(all_posts))
    comment = 'New comment!!!'
    oxwall.post_comment(comment)
    comment_list = driver.find_elements(*DashboardPageLocators.LIST_OF_COMMENTS)
    oxwall.wait_new_comment_appear(len(comment_list))
    comment_list2 = driver.find_elements(*DashboardPageLocators.LIST_OF_COMMENTS)

    assert comment_list2[0].text == comment


def test_delete_message(oxwall, driver, logged_user):
    time.sleep(2)
    post_blocks_list = oxwall.press_menu_button_in_post()
    oxwall.press_delete_button()
    oxwall.confirm_alert()
    time.sleep(1)
    post_blocks_list2 = driver.find_elements(*DashboardPageLocators.LIST_OF_POST_BLOCKS)
    assert post_blocks_list[-2] == post_blocks_list2[-1]


def test_signup(oxwall, driver, wait):
    user = User(username="Test1", password="pass", real_name="TESTER", email="test@test.com", gender="2",
                birthday=date(2000, 12, 16))

    oxwall.click_signup_button()
    oxwall.input_username_email_password('Testuser8', 'test8@test.com', 'q123456_')
    oxwall.press_male_radiobutton()
    oxwall.select_day_month_year('24', 'Apr', '1981')
    oxwall.check_male_fun()
    oxwall.fill_in_textareas(music='rock and some another heavy music', books='fantasy')
    oxwall.upload_photo()
    oxwall.submit()

    welcome = wait.until(expected_conditions.visibility_of_element_located(
        DashboardPageLocators.LOGIN_CONFIRM)
    )

    assert welcome.is_displayed() == True
