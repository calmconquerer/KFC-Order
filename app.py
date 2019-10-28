from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import exports

options = webdriver.FirefoxOptions()
# options.add_argument("-headless")

driver = webdriver.Firefox(options=options)


def navigation():
    driver.get('https://www.kfcpakistan.com')
    WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/app-header/header/div/div[2]/app-nav/div/div[3]")))
    driver.find_element(By.XPATH,
                        '/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/app-header/header/div/div[2]/app-nav/div/div[3]').click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/div/app-collections/div/div[2]/div/div/div/product-card[3]/div/div[2]/div[2]/button')))
    wow_box = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/div/app-collections/div/div[2]/div/div/div/product-card[3]/div/div[2]/div[2]/button")
    wow_box.click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/div/app-product/div/div[2]/div[2]/div[3]/div[2]/div[2]/button')))
    add_to_bucket = driver.find_element(By.XPATH, '/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/div/app-product/div/div[2]/div[2]/div[3]/div[2]/div[2]/button')
    add_to_bucket.click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, "mat-select-value")))
    city_option = driver.find_element(By.CLASS_NAME, "mat-select-value")
    city_option.click()

    islamabad = driver.find_element(By.XPATH, '//*[@id="mat-option-7"]')
    islamabad.click()
    location = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
    location.send_keys(exports['Location'])
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-option-28"]')))
    driver.find_element(By.XPATH, '//*[@id="mat-option-28"]').click()
    next = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav/kfc-cart/div/div[2]/div/div/button")
    next.click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav/kfc-cart/div/div[5]/button")))
    checkout = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav/kfc-cart/div/div[5]/button")
    checkout.click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEmailA"]')))
    # check_out_as_guest = driver.find_element(By.XPATH,
    #                                          "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/div/app-checkout/div/div[2]/div[2]/div[1]/div[1]/mat-card/form/mat-card-content[1]/mat-button-toggle-group/mat-button-toggle[2]/label/div")
    # check_out_as_guest.click()
    email_input = driver.find_element(By.XPATH, '//*[@id="frmEmailA"]')
    email_input.send_keys(exports['Email_Address'])

    continue_as_guest = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/div/app-checkout/div/div[2]/div[2]/div[1]/div[1]/mat-card/form/mat-card-content[3]/button")
    continue_as_guest.click()

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable, '//*[@id="frmNameA"]')

    full_name = driver.find_element(By.XPATH, '//*[@id="frmNameA"]')
    full_name.send_keys(exports['Full_Name'])

    address = driver.find_element(By.XPATH, '//*[@id="frmAddressS"]')
    address.send_keys(exports['Address'])

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-input-5"]')))
    phone_input = driver.find_element(By.XPATH, '//*[@id="mat-input-5"]')
    phone_input.send_keys(exports['Phone_Number'])
    time.sleep(5)

    continue_to_payment = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/div/app-checkout/div/div[2]/div[2]/div[1]/div[2]/form/mat-card/mat-card-content[2]/button")
    continue_to_payment.click()

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable, '//*[@id="mat-radio-9"]')
    cash_on_delivery = driver.find_element(By.XPATH, '//*[@id="mat-radio-9"]')
    cash_on_delivery.click()
    time.sleep(5)
    place_order = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/app-base/mat-sidenav-container/mat-sidenav-content/div/app-checkout/div/div[2]/div[2]/div[1]/div[3]/form/div/div/mat-card/mat-card-content/button")
    place_order.click()


try:
    print('initialized')
    navigation()
finally:
    print('working')
    driver.quit()
