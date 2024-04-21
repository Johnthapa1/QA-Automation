import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Functions to check if a string is a valid email address
def is_valid_email (email):
    try:
        # check email format using RE
        email_pattern = "/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/"
        if re.search(email_pattern, email):
            return True
        else:
            return False

# Function to check if a string is a valid phone number
def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$', phone))

# Open the web page
driver.get("https://technomax.com.np")
driver.maximize_window()

# Set the scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

# loop to keep scrooling

