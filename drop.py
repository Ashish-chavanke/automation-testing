from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

# Step 1: Open dropdown page
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
time.sleep(2)

# Step 2: Switch to iframe
driver.switch_to.frame("iframeResult")

# Step 3: Handle dropdown
dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_visible_text("Saab")
time.sleep(2)

# Step 4: Open checkbox page
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
time.sleep(2)

# Step 5: Handle checkbox
checkbox = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
checkbox.click()
time.sleep(2)

# Step 6: Close browser
driver.quit()