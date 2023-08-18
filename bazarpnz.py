import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://bazarpnz.ru/add.php")
    time.sleep(3)
    browser.get("http://bazarpnz.ru/add.php?main")
    # button = browser.find_element(By.ID, "submit_button")
    time.sleep(3)
finally:
    browser.quit()
