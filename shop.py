# # отображение страницы товара
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
# driver.find_element_by_css_selector('#menu-item-50 a').click()
# time.sleep(1)
# driver.find_element_by_id('username').send_keys('1234@yandex.ru')
# driver.find_element_by_id('password').send_keys('QaWsEdRf*951')
# driver.find_element_by_css_selector('input[value="Login"]').click()
# # 3
# driver.find_element_by_css_selector('#menu-item-40 a').click()
# # 4
# driver.find_element_by_css_selector('.post-181 a').click()
# # 5
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".summary.entry-summary h1"), 'HTML5 Forms'))
#
# driver.quit()

# # количество товаров в категории
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
# driver.find_element_by_css_selector('#menu-item-50 a').click()
# time.sleep(1)
# driver.find_element_by_id('username').send_keys('1234@yandex.ru')
# driver.find_element_by_id('password').send_keys('QaWsEdRf*951')
# driver.find_element_by_css_selector('input[value="Login"]').click()
# # 3
# driver.find_element_by_css_selector('#menu-item-40 a').click()
# time.sleep(1)
# # 4
# driver.find_element_by_css_selector('.cat-item.cat-item-19 a').click()
# time.sleep(1)
# # 5
# assert len(driver.find_elements_by_css_selector('.products>li'))) == 3
#
# driver.quit()

# сортировка товаров
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
# driver.find_element_by_css_selector('#menu-item-50 a').click()
# time.sleep(1)
# driver.find_element_by_id('username').send_keys('1234@yandex.ru')
# driver.find_element_by_id('password').send_keys('QaWsEdRf*951')
# driver.find_element_by_css_selector('input[value="Login"]').click()
# # 3
# driver.find_element_by_css_selector('#menu-item-40 a').click()
# time.sleep(1)
# # 4
# selector_sort = driver.find_element_by_class_name("orderby")
# selector_sort_value = selector_sort.get_attribute('value')
# assert selector_sort_value == "menu_order"
# # 5
# select = Select(selector_sort)
# select.select_by_value("price-desc")
# # 6
# selector_sort = driver.find_element_by_class_name("orderby")
# selector_sort_value = selector_sort.get_attribute('value')
# # 7
# assert selector_sort_value == "price-desc"
#
# driver.quit()

# отображение, скидка товара
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
# driver.find_element_by_css_selector('#menu-item-50 a').click()
# time.sleep(1)
# driver.find_element_by_id('username').send_keys('1234@yandex.ru')
# driver.find_element_by_id('password').send_keys('QaWsEdRf*951')
# driver.find_element_by_css_selector('input[value="Login"]').click()
# # 3
# driver.find_element_by_css_selector('#menu-item-40 a').click()
# time.sleep(1)
# # 4
# driver.find_element_by_css_selector('.post-169 h3').click()
# # 5
# old_price = driver.find_element_by_css_selector('.price > del > span')
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# # 6
# new_price = driver.find_element_by_css_selector('.price > ins > span')
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
# # 7
# book_cover = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'images')))
# book_cover.click()
# # 8
# btn_close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
# btn_close.click()
#
# driver.quit()

# проверка цены в корзине
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
# driver.find_element_by_css_selector('#menu-item-40 a').click()
# # 3
# driver.find_element_by_css_selector('.post-182 [rel="nofollow"]').click()
# # 4
# time.sleep(5)
# cart_count = driver.find_element_by_css_selector('span.cartcontents')
# cart_count_text = cart_count.text
# cart_price = driver.find_element_by_css_selector('span.amount')
# cart_price_text = cart_price.text
# assert cart_count_text == "1 Item"
# assert cart_price_text == "₹180.00"
# # 5
# driver.find_element_by_class_name('wpmenucart-contents').click()
# # 6
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal .woocommerce-Price-amount'), '180.00'))
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total .woocommerce-Price-amount'), '189.00'))
#
# driver.quit()

# работа в корзине
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
# driver.find_element_by_css_selector('#menu-item-40 a').click()
# # 3
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector('.post-182 [rel="nofollow"]').click()
# time.sleep(1)
# driver.find_element_by_css_selector('.post-180 [rel="nofollow"]').click()
# # 4
# time.sleep(3)
# driver.find_element_by_class_name('wpmenucart-contents').click()
# # 5
# time.sleep(3)
# driver.find_element_by_css_selector('tr:nth-child(1) a.remove').click()
# # 6
# time.sleep(5)
# driver.find_element_by_css_selector('.woocommerce-message a').click()
# # 7
# driver.find_element_by_css_selector('tr:nth-child(1) input').clear()
# driver.find_element_by_css_selector('tr:nth-child(1) input').send_keys('3')
# # 8
# driver.find_element_by_name('update_cart').click()
# # 9
# count_item = driver.find_element_by_css_selector('tr:nth-child(1) input')
# assert count_item.get_attribute("value") == "3"
# # 10
# time.sleep(1)
# driver.find_element_by_css_selector('input[name="apply_coupon"]').click()
# # 11
# wait.until(EC.text_to_be_present_in_element((By.ID, 'page-34'), 'Please enter a coupon code'))
#
# driver.quit()

# покупка товара
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
driver.find_element_by_css_selector('#menu-item-40 a').click()
# 3
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector('.post-182 [rel="nofollow"]').click()
# 4
time.sleep(3)
driver.find_element_by_class_name('wpmenucart-contents').click()
# 5
btn_forward = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'wc-forward')))
btn_forward.click()
# 6
wait.until(EC.visibility_of_element_located ((By.ID, 'billing_first_name'))).send_keys('Ivan')
time.sleep(1)
wait.until(EC.visibility_of_element_located ((By.ID, 'billing_last_name'))).send_keys('Petrov')
#driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_id('billing_email').send_keys('1234@yandex.ru')
driver.find_element_by_id('billing_phone').send_keys('1234567890')
driver.find_element_by_id('select2-chosen-1').click()
driver.find_element_by_class_name('select2-input').send_keys('russ')
driver.find_element_by_class_name('select2-result-label').click()
driver.find_element_by_css_selector('#billing_address_1.input-text').send_keys("какая то улица")
driver.find_element_by_css_selector('#billing_city.input-text').send_keys('какой то город')
driver.find_element_by_css_selector('#billing_state.input-text').send_keys('какая то область')
driver.find_element_by_css_selector('#billing_postcode.input-text ').send_keys('442240')
# 7
driver.execute_script("window.scrollBy(0, 700);")
time.sleep(3)
driver.find_element_by_id('payment_method_cheque').click()
# 8
driver.find_element_by_id('place_order').click()
# 9
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'page-id-35'), 'Thank you. Your order has been received.'))
# 10
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li:nth-child(4) strong'), 'Check Payments'))

driver.quit()