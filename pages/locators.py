from selenium.webdriver.common.by import By


class DashboardPageLocators:
    POST_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")
    LOGIN_CONFIRM = (By.XPATH, '//div[@class="ow_box_cap_body"]/h3[@class="ow_ic_info"]')
    LIST_OF_ALL_POSTS = (By.XPATH, '//div[@class="ow_newsfeed_content ow_smallmargin"]')
    LIST_OF_USERS_IN_POSTS = (By.XPATH, '//div[@class="ow_newsfeed_string ow_small ow_smallmargin"]/a/b')
    LIST_OF_COMMENTS = (By.XPATH, '//div[@class="ow_comments_content ow_smallmargin"]')
    LIST_OF_POST_BLOCKS = (By.XPATH, '//div[@class="ow_newsfeed_context_menu_wrap"]')


class HeaderLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//span[@class="ow_signin_label"]')
    SIGN_UP_BUTTON = (By.XPATH, '//a[text()="Sign up"]')
    MAIN_MENU = ()
    JOIN_MENU = ()


class LoginPageLocators:
    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.NAME, "submit")


class PostLocators:
    TEXT_AREA_FOR_POST = (By.NAME, 'status')
    POST_TEXT = ""
    POST_USER = ""
    POST_TIME = ""
    MENU_BUTTON_LIST = (By.XPATH, '//div[@class="ow_newsfeed_context_menu"]')
    DELETE_BUTTON_LIST = (By.XPATH, '//a[@class="newsfeed_remove_btn owm_red_btn"]')
    COMMENT_BUTTON_LIST = (By.XPATH, '//span[@class="ow_miniic_comment newsfeed_comment_btn "]')
    COMMENT_TEXT_FIELD_LIST = (By.XPATH, '//textarea[@class="comments_fake_autoclick"]')


class JoinLocators:
    USER_NAME_FIELD = (By.XPATH, '//input[@class="ow_username_validator" and contains (@type, text)]')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password" and contains (@type, password)]')
    PASSWORD_REPEAT_FIELD = (By.XPATH, '//input[@name="repeatPassword" and contains (@type, password)]')
    REAL_NAME_FIELD = (By.XPATH, '//input[@type="text"]')
    MALE_RADIO = (By.XPATH, '//input[@type="radio" and contains (@value, "1")]')
    BIRTH_COMBO_LIST = (By.XPATH, '//div[@class="ow_inline owm_inline"]/select[@type="text"]')
    MALE_CHECKBOX = (By.XPATH, '//ul[@class="ow_checkbox_group clearfix"]/li/label[text()="Male"]')
    FUN_CHECKBOX = (By.XPATH, '//ul[@class="ow_checkbox_group clearfix"]/li/label[text()="Fun"]')
    TEXTAREA_LIST = (By.XPATH, '//textarea')
    PHOTO_BLOCK = (By.XPATH, '//input[@name="userPhoto" and contains (@type, "file")]')
    APPLY_CROP_BUTTON = (By.ID, 'avatar-crop-btn')
    JOIN_BUTTON = (By.NAME, 'joinSubmit')