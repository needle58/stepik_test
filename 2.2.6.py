import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    x = browser.find_element(By.ID, 'input_value').text
    ans = str(math.log(abs(12 * math.sin(int(x)))))
    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(ans)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    browser.execute_script("window.scrollBy(0, 100);")
    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()
    button = browser.find_element(By.CLASS_NAME, 'btn')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
