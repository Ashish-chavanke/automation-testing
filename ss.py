from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open Wikipedia
driver.get("https://www.wikipedia.org")
time.sleep(3)

# Search shoes
search = driver.find_element(By.NAME, "search")
search.send_keys("shoes")
search.send_keys(Keys.RETURN)

time.sleep(4)

# Click first result
result = driver.find_element(By.XPATH, "(//a)[1]")
result.click()

time.sleep(4)

# Take screenshot
driver.save_screenshot("C:\\Users\\Ashish\\OneDrive\\Desktop\\shoes.png")

driver.quit()