from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://satee143:password@www.engprod-charter.net')
driver.switch_to.alert.dismiss()
driver.execute_script()