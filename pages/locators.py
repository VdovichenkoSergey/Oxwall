from selenium.webdriver.common.by import By


class DashboardPageLocators:
    POST_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")


class HeaderLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//span[@class="ow_signin_label"]')
    SIGN_UP_BUTTON = ()
    MAIN_MENU = ()
    JOIN_MENU = ()


class LoginPageLocators:
    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.NAME, "submit")
