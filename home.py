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
driver.execute_script("window.scrollBy(0, 600);")
# 3
driver.find_element_by_css_selector("[title='Selenium Ruby']").click()
# 4
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element_by_css_selector('.reviews_tab a').click()
# 5
time.sleep(1)
driver.find_element_by_class_name("star-5").click()
# 6
driver.find_element_by_id("comment").send_keys("Nice book!")
# 7
driver.find_element_by_id("author").send_keys("Petrov")
# 8
driver.find_element_by_id("email").send_keys("123@yandex.ru")
# 9
time.sleep(1)
driver.find_element_by_id("submit").click()

driver.quit()