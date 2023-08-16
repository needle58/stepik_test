import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    string = browser.find_element(By.TAG_NAME, 'img')
    x = string.get_attribute("valuex")
    txt_field = browser.find_element(By.ID, 'answer')
    txt_field.send_keys(calc(x))

    chkbox = browser.find_element(By.ID, 'robotCheckbox')
    chkbox.click()

    radbtn = browser.find_element(By.ID, 'robotsRule')
    radbtn.click()

    baton = browser.find_element(By.CLASS_NAME, 'btn')
    baton.click()
finally:
    time.sleep(5)
    browser.quit()
