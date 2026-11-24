# drag & drop automation
#import webdiver
from selenium import webdriver  #import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains

import time

driver=webdriver.Chrome()  #initalize whroe with wedbdriver

time.sleep(1)   #timer set to 1sec after 1 sec google open

driver.maximize_window()  #maximize window

url="http://formy-project.herokuapp.com/dragdrop"
driver.get(url)

time.sleep(2)

source=driver.find_element(By. XPATH,"//div[@id='image']//img")

destination=driver.find_element(By. XPATH,"//div[@id='box']")

actions=ActionChains(driver)

actions.drag_and_drop(source, destination).perform()

driver.quit()