from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Step 1: Open alert demo page
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
time.sleep(2)

# Step 2: Switch to iframe
driver.switch_to.frame("iframeResult")

# Step 3: Click button to trigger alert
driver.find_element(By.XPATH, "//button").click()
time.sleep(2)

# Step 4: Switch to alert
alert = driver.switch_to.alert

# Step 5: Accept alert (OK)
alert.accept()

time.sleep(2)

# Step 6: Close browser
driver.quit()