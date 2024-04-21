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
        email_pattern = "^[a-z]+[\._]?[a-z 0-9]+[@]\w[.]\w{2,3}$"
        if re.search(email_pattern, email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False



# Function to check if a string is a valid phone number
def is_valid_phone (phone):
    return bool(re.match(r'^\d{10}$', phone))

# Open the web page
driver.get("https://mindrisers.com.np/contact-us")
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




# Explicitly wait for the email field to be clickable

email_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(driver.find_element(*(By.XPATH,"//input[@placeholder='Email']")))
)
# time.sleep(10)
# Explicitly wait for the phone number field to be clickable

phone_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']")))
)



# valid email for testing
email = "test_123@gmail.com"
phone= "987654345"


# Add a sleep to see the form filling action

time.sleep(10)



# Check if the email address is valid

if is_valid_email(email):
    print("valid email address")

else:
    print("Invalid email address")

# Clear the field and enter the email value
email_field.clear()
email_field.send_keys(email)

time.sleep(1)

# Check if phone number is empty

if not phone:
    print("Phone number cannot be empty")

    # Clear the field and enter the phone number value

phone_field.clear()
phone_field.send_keys(phone)
time.sleep(1)



driver.quit()