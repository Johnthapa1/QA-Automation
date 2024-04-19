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