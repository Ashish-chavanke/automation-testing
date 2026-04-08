from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Step 1: Open form page
driver.get("https://www.w3schools.com/html/html_forms.asp")
time.sleep(2)

# Step 2: Fill form data
fname = driver.find_element(By.ID, "fname")
fname.clear()
fname.send_keys("Ashish")

lname = driver.find_element(By.ID, "lname")
lname.clear()
lname.send_keys("Chavanke")

time.sleep(2)

# Step 3: Submit form
submit = driver.find_element(By.XPATH, "//input[@type='submit']")
submit.click()

time.sleep(3)

# Step 4: Close browser
driver.quit()