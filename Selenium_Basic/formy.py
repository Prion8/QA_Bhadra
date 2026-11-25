from selenium import webdriver  #import webdriver

from selenium.webdriver.common.by import By

import time

# from selenium.webdriver.support.ui import WebDriverWait  #WebDriverWait is class

# from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()  #initalize whroe with wedbdriver

time.sleep(1)   #timer set to 1sec after 1 sec google open

driver.maximize_window()  #maximize window

url="https://formy-project.herokuapp.com/switch-window"

driver.get(url)

time.sleep(2)

#switch window
switch_window=driver.find_element(By.ID,"new-tab-button")
switch_window.click()

time.sleep(2)

#window handles
print(driver.window_handles)

windows=driver.window_handles

print(windows)

print("The driver is in", driver.current_window_handle)

#switch windows
driver.switch_to.window(windows[1])
print("The driver is in", driver.current_window_handle)

print(driver.current_window_handle)


driver.quit()