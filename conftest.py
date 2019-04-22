from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Utils import util
import unittest


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture(scope='class')
def Browser_setup(request):
    browser = request.config.getoption('--browser')
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(util.URL)



    yield
    #driver.close()
    #driver.quit()




