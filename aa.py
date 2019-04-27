from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest_dependency
import pytest
import unittest
import time
from webdriver_manager import utils
from selenium.webdriver.common.by import By



driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.cleartrip.com')
driver.find_element(by=By.ID,value='FromTag').send_keys('bangalore')

#//*[@id="fli_list_item0"]/div[1]/div/div/div/div[3]/p/span/span/text()
#//div[contains(@class,'preferred')]//div[@class='price-group']//span[2]
#//div[contains(@class,'preferred')]//div[contains(@class,'group')]//span[2]