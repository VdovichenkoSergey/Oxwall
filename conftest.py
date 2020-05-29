import pytest
from selenium import webdriver
from oxwall_helper import OxwallHelper


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
def loged_user(oxwall):
    login = 'admin'
    oxwall.wait_signin()
    oxwall.sign_in(login=login, password='pass')
    return login


with open('messages.txt', 'r', encoding='utf-8') as output:
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
