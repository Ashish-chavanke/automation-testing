from selenium import webdriver
import time

driver = webdriver.Chrome()

# Step 1: Open first website
driver.get("https://www.google.com")
time.sleep(2)

# Step 2: Open second website
driver.get("https://www.wikipedia.org")
time.sleep(2)

# Step 3: Go back
driver.back()
time.sleep(2)

# Step 4: Go forward
driver.forward()
time.sleep(2)

# Step 5: Refresh page
driver.refresh()
time.sleep(2)

# Step 6: Close browser
driver.quit()