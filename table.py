from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open table page
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(2)

# Get all rows (skip header)
rows = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")[1:]

# Extract data
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    print(cols[0].text, cols[1].text, cols[2].text)

driver.quit()