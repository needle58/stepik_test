import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    ans = calc(x)
    pole = browser.find_element(By.ID, 'answer')
    pole.send_keys(ans)
    chbox = browser.find_element(By.ID, 'robotCheckbox')
    chbox.click()
    radiobtn = browser.find_element(By.ID, 'robotsRule')
    radiobtn.click()
    btn = browser.find_element(By.CSS_SELECTOR, '.btn')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
