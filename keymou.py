from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
# Open site
driver.get("https://www.wikipedia.org")
time.sleep(3)
# Find search box
search_box = driver.find_element(By.NAME, "search")
actions = ActionChains(driver)
# Keyboard action
actions.click(search_box)
actions.send_keys("Selenium")
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(4)
# Mouse action (RIGHT CLICK visible)
heading = driver.find_element(By.ID, "firstHeading")
actions.move_to_element(heading).perform()
time.sleep(2) # SEE mouse move
actions.context_click(heading).perform()
time.sleep(3)
driver.quit()