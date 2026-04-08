from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Implicit Wait
driver.implicitly_wait(100)

# Open website
driver.get("https://www.google.com")

# Locate search box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Waits")
search_box.send_keys(Keys.RETURN)

# Explicit Wait (wait for results)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "search")))

driver.quit()