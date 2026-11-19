from selenium import webdriver  #import webdriver

import time

driver=webdriver.Chrome()  #initalize whroe with wedbdriver

time.sleep(1)   #timer set to 1sec after 1 sec google open

driver.maximize_window()  #maximize window

url="https://www.google.com/"

driver.get(url)

time.sleep(2)

print("The current URL is",driver.current_url)
print("The page title is", driver.title)

driver.get("https://www.saucedemo.com/")

time.sleep(1)

print("The current URL is",driver.current_url)
print("The page title is", driver.title)

driver.refresh()

time.sleep(1)

driver.back()

time.sleep(1)

driver.forward()

time.sleep(1)

driver.quit() #quit driver