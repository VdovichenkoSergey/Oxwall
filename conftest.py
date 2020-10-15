import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from db.db_connector import OxwallDB
from oxwall_helper import OxwallHelper
from pages.internal_pages.main_page import MainPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.0.191/oxwall/')
    return driver


@pytest.fixture()
def oxwall(driver):
    return OxwallHelper(driver)


@pytest.fixture()
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture()
def logged_user(oxwall):
    login = 'admin'
    oxwall.wait_signin()
    oxwall.sign_in(login=login, password='pass')
    return login


with open('messages.txt', 'r') as output:
    mess_list2 = output.readlines()
    message_list = []
    for m in mess_list2:
        m2 = m.rstrip("\n")
        message_list.append(m2)
    output.close()


@pytest.fixture(params=message_list, ids=[str(i) for i in message_list])  # parametrization
def message_list(request):
    message = request.param
    return message


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def db():
    db = OxwallDB()
    yield db
    db.close()
