from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close()

# fire_browser.get('https://www.seleniumeasy.com/tags/allure')

# assert "Allure" in fire_browser.title
# allure_btn = fire_browser.find_element(By.CLASS_NAME, "active")
# print(allure_btn.get_attribute('innerHTML'))

# fire_browser.close()