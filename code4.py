from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# setup chrome webdriver using webdriver manager
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the URL of the website to visit
website_url= 'https://khalti.com/'
# Open the website
driver.get(website_url)
driver.maximize_window()
time.sleep(5)

# Calculate the height of the webpage using javascript
page_height = driver.execute_script("return document.body.scrollHeight")

# Scroll down the webpage slowly using javascript
scroll_speed = 100
scroll_iterations = int(page_height / scroll_speed)

# Loop to perform scrolling in increments
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
    time.sleep(1)

website_title= driver.title
print(f"Website Title:{website_title}")

driver.close()
driver.quit()