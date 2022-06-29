# # регистрация аккаунта
# import time
# import driver as driver
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
# # 1
# driver.get("http://practice.automationtesting.in/")
# # 2
# time.sleep(1)
# driver.find_element_by_css_selector('#menu-item-50 a').click()
# # 3
# time.sleep(1)
# driver.find_element_by_id('reg_email').send_keys('1234@yandex.ru')
# # 4
# time.sleep(1)
# driver.find_element_by_id('reg_password').send_keys('QaWsEdRf*951')
# # 5
# time.sleep(3)
# driver.find_element_by_css_selector('input[value="Register"]').click()
#
# driver.quit()

# логин в систему
import time
import driver as driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
# 1
driver.get("http://practice.automationtesting.in/")
# 2
time.sleep(1)
driver.find_element_by_css_selector('#menu-item-50 a').click()
# 3
time.sleep(1)
driver.find_element_by_id('username').send_keys('1234@yandex.ru')
# 4
time.sleep(1)
driver.find_element_by_id('password').send_keys('QaWsEdRf*951')
# 5
driver.find_element_by_css_selector('input[value="Login"]').click()
time.sleep(3)
# 6
wait.until(EC.text_to_be_present_in_element((By.ID, "body"), 'Logout'))
driver.quit()