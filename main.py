from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# Set UP the Chrome WebDriver using WebDriver Manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager() . install ( ) ) )

try:
    # URL of the website you want to open
    website_url='https://merolagani.com/'

    # Open the website
    driver.get(website_url)
    time.sleep(5)
    # Maximize the browser window
    driver. maximize_window()
    # Wait for 7 seconds to see the website content
    time.sleep (7)
    # Extract and print the website title
    website_title = driver.title
    print(f"Website Title:{website_title}")
finally:

    driver. quit()