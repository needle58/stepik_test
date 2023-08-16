import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    ans = str(num1 + num2)
    fall_list = Select(browser.find_element(By.TAG_NAME, 'select'))
    fall_list.select_by_value(num1 + num2)
finally:
    browser.quit()
