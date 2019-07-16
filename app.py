from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import config

driver = webdriver.Firefox()
imp_wait = driver.implicitly_wait(5)


def navigation():
    driver.get('https://www.kfcpakistan.com')
    driver.find_element(By.XPATH, '(//*[@id="dropdownTest"])[2]').click()



try:
    print('initialized')
    navigation()
finally:
    print('working')
    # driver.quit()