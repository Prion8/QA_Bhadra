from selenium import webdriver  #import webdriver

from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome()  #initalize whroe with wedbdriver

time.sleep(1)   #timer set to 1sec after 1 sec google open

driver.maximize_window()  #maximize window

url="https://www.saucedemo.com/"

driver.get(url)

driver.implicitly_wait(20) # waits Max 20 sec until command runs

time.sleep(2)


# username= driver.find_element(By.ID,"user-name")  #find by ID

username= driver.find_element(By.XPATH,"//*[@id='user-name']")  #find locator by Xapth


password= driver.find_element(By.ID,"password")

login_button= driver.find_element(By.ID,"login-button")

#Action
username.send_keys("standard_user")

time.sleep(2)
password.send_keys("secret_sauce")

login_button.screenshot("Login_button.png")

login_button.click()

driver.save_screenshot("login.png")

time.sleep(2)

# assert driver.current_url=="https://www.saucedemo.com/inventory.html","Login failed"
assert "inventory" in driver.current_url,"login Failed"
print("Login Successful")
driver.quit()