import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element(By.CLASS_NAME, 'trollface').click()
    print(browser.window_handles[0])
    print(browser.window_handles[1])
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(10)
    browser.quit()
