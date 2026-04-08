from selenium import webdriver

# Step 1: Initialize Firefox WebDriver
driver = webdriver.Firefox()

# Step 2: Open website
driver.get("https://www.google.com")

# Step 3: Verify by printing title
print("Page Title:", driver.title)

# Step 4: Close browser
driver.quit()