from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import unittest
from webdriver_manager import utils

class Test(unittest.TestCase):
    def test_a(self):
        self.assertNotEqual(5,5)


s=Test()
s.test_a()

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
# print(driver.find_element_by_tag_name('p').text)