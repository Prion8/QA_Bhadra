# SacuceDemo login automation
#import webdiver
from selenium import webdriver  #import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC 


#import time

driver=webdriver.Chrome()  #initalize whroe with wedbdriver

#time.sleep(1)   #timer set to 1sec after 1 sec google open

driver.maximize_window()  #maximize window

url="https://www.saucedemo.com/"

driver.get(url)

#time.sleep(2)

'''
username= user-name
pasword=password
login_botton=login-button

XPATH Locator

username=
Relative XPATH
//*[@id="user-name"]

Absolute XPATH
/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input

password=
Relative XPATH
//*[@id="password"]

Absolute XPATH
/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input

Login_button=
Relative XPATH
//*[@id="login-button"]

Absolute XPATH
/html/body/div/div/div[2]/div[1]/div/div/form/input
'''
# username= driver.find_element(By.ID,"user-name")  #find by ID

wait=WebDriverWait(driver,10)

#Locate username
username=wait.until(EC.visibility_of_element_located((By.ID,"user-name"))
)

# Locate password
password = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)

# Locate login_button
login_button = wait.until(
    EC.element_to_be_clickable((By.ID,"login-button"))
)

# username= driver.find_element(By.XPATH,"//*[@id='user-name']")  #find locator by Xapth


# password= driver.find_element(By.ID,"password")

# login_button= driver.find_element(By.ID,"login-button")

#Action
username.send_keys("standard_user")

#time.sleep(2)
password.send_keys("secret_sauce")

#actions chains or mouse actions
action=ActionChains(driver)

action.click(login_button).perform()

wait.until(EC.url_contains("inventory.html"))

assert "inventory.html" in driver.current_url

print("Login successful")

product_sort=driver.find_element(By.CLASS_NAME,"product_sort_container")

sort=Select(product_sort)

sort.select_by_visible_text("Price (low to high)")

# login_button.click()

#time.sleep(2)

driver.quit()
