from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import config

driver = webdriver.Firefox()


def navigation():
    driver.get('https://www.kfcpakistan.com')
    driver.find_element(By.XPATH, '(//*[@id="dropdownTest"])[3]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/app-collections/div/div[2]/div/div/div/product-card[3]/div/div[2]/div[2]/button').click()
    driver.find_element(By.CSS_SELECTOR, 'body > app-root > div:nth-child(1) > app-base > mat-sidenav-container > mat-sidenav-content > app-product > div > div:nth-child(3) > div.productInfo > div.pt-2.ng-star-inserted > div.row > div:nth-child(2) > button').click()
    driver.find_element(By.XPATH, '/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav/kfc-cart/div/div[2]/div/div/mat-form-field[1]/div/div[1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="mat-option-7"]').click()
    driver.find_element(By.XPATH, '//*[@id="mat-select-1"]/div/div[1]').click()
    driver.find_element(By.XPATH, '//*[@id="mat-option-58"]').click()
    driver.find_element(By.XPATH, '//*[@id="mat-select-2"]/div/div[1]').click()



try:
    print('initialized')
    navigation()
finally:
    print('working')
    # driver.quit()