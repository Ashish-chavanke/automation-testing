from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open website
driver.get("https://www.wikipedia.org")
time.sleep(2)

# Locate using ID
search_box = driver.find_element(By.ID, "searchInput")

# Enter text
search_box.send_keys("Selenium")

# Locate using CSS Selector and click
button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

time.sleep(3)

# Locate using XPath (heading)
heading = driver.find_element(By.XPATH, "//h1")
print("Heading:", heading.text)

driver.quit()