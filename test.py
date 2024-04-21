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
def is_valid_phone (phone):
    return bool(re.match(r'^\d{10}$', phone))

# Open the web page
driver.get("https://technomax.com.np")
driver.maximize_window()

# Set the scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Explicitly wait for the first name field to be clickable

first_name_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "form_name"))
)

# Explicitly wait for the last name field to be clickable

last_name_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "form_name"))
)

# Explicitly wait for the email field to be clickable

email_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "form_email"))
)
time.sleep(5)
# Explicitly wait for the phone number field to be clickable

phone_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "form_phone"))
)
# Explicitly wait for the message field to be clickable
message_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "form_message"))
)

# Example Values
first_name = ""
last_name = "test"

# Invalid email for testing

# email = "johndoe"
# email="johndoe@@gmail.com"
# email="johndoe@@gmail"
# email="johndoe@@gmail..com"

# valid email for testing
email = "test1234@gmail.com"
phone= "987654345"
message= "Hello this is test 123"

# Add a sleep to see the form filling action

time.sleep(5)

# check if the first_name is empty

if not first_name:
    print("Name cannot be empty")

    # clear the field and enter the first name value

first_name_field.clear()
first_name_field.send_keys(first_name)

time.sleep(0.75)

# Clear the field and enter the last name values

last_name_field.clear()
last_name_field.send_keys(last_name)

time.sleep(0.75)

# Check if the email address is valid

if is_valid_email(email):
    print("valid email address")

else:
    print("Invalid email address")

# Clear the field and enter the email value
email_field.clear()
email_field.send_keys(email)

time.sleep(0.75)

# Check if phone number is empty

if not phone:
    print("Phone number cannot be empty")

    # Clear the field and enter the phone number value

phone_field.clear()
phone_field.send_keys(phone)
time.sleep(0.75)

# clear the field and enter the message value
message_field.clear()
message_field.send_keys(message)

driver.quit()