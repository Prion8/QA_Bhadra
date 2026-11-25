from selenium import webdriver  #import webdriver

from selenium.webdriver.common.by import By

import time

# from selenium.webdriver.support.ui import WebDriverWait  #WebDriverWait is class

# from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()  #initalize whroe with wedbdriver

time.sleep(1)   #timer set to 1sec after 1 sec google open

driver.maximize_window()  #maximize window

url="https://formy-project.herokuapp.com/scroll"

driver.get(url)

#scroll
driver.execute_script("window.scrollBy(0,700);")

time.sleep(2)

driver.find_element(By.ID,"name").send_keys("Beatles")

driver.find_element(By.ID,"date").send_keys("10/10/1969")

time.sleep(2)

driver.execute_script("window.scrollTo(0,0);")

time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHright);")

time.sleep(2)

driver.quit()