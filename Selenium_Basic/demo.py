from selenium import webdriver

import time
driver=webdriver.Chrome()

url="https://www.google.com/"

driver.get(url)

google_title = driver.title

print("The page title is:",google_title)

driver.get("https://www.saucedemo.com/")

actual_title = driver.title

assert actual_title== "Swag Labs"

print("test passed")

