from selenium import webdriver  #import webdriver

from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome()  #initalize whroe with wedbdriver

time.sleep(1)   #timer set to 1sec after 1 sec google open

#driver.maximize_window()  #maximize window

url="http://sagar-test-qa.vercel.app/"

driver.get(url)

time.sleep(2)


# username= driver.find_element(By.ID,"user-name")  #find by ID

username= driver.find_element(By.ID,"username")  #find locator by Xapth


password= driver.find_element(By.ID,"password")

login_button= driver.find_element(By.XPATH,"//button[@type='submit']")

#Action
username.send_keys("standard_user")

time.sleep(2)
password.send_keys("secret_sauce")

login_button.click()

time.sleep(2)
alert=driver.switch_to.alert
alert.accept()
#alert.dismiss()
driver.quit()
