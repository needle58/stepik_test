import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    book_button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    book_button.click()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(10)
    browser.quit()
