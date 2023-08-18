import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]').send_keys("Govnov")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]').send_keys("iamreal@ebanat.com")

    current_dir = os.path.abspath(os.path.dirname('D:\\'))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '123.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(10)
    browser.quit()
