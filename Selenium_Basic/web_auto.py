from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

driver=webdriver.Chrome()

# time.sleep(5)

url="https://sagar-test-qa.vercel.app/contact.html"

driver.get(url)

time.sleep(1)

# Locate the name box
name=driver.find_element(By.ID,"name")

# Locate the email box
email=driver.find_element(By.ID,"email")

send_button=driver.find_element(By.XPATH,"//button[@type='submit']")   #XPATH,"//button[@type='submit']")

# Locate the input box or textarea
message_box=driver.find_element(By.ID,"message")

# Type the full name
name.send_keys("karen sha")

# Type the email address
email.send_keys("mindrisers@gmail.com")

# Clear any existing text (optional)
message_box.clear()

# Type the message
message_box.send_keys("Hello, this is my message!")

# Press Enter to send (optional)
message_box.send_keys(Keys.RETURN)

# Wait for 3sec
time.sleep(3)


send_button.click()


time.sleep(1)

link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[href="https://www.linkedin.com/in/yourname"]')
    )
)
link.click()

driver.quit()