# import necessary modules from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# set up the chrome webdriver using webdriver manager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # URL of the website you want to open
    website_url = 'https://merolagani.com/NewsList.aspx'
    # open the website
    driver.get(website_url)
    time.sleep(5)
    # maximize the browser window
    driver.maximize_window()
    # wait for 7 seconds to see the website content
    time.sleep(7)
# extract and print the website content
    website_title = driver.title
    print(f"Website Title: {website_title}")

finally:
    # Close the webDriver instance
    driver.quit()
