from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By module for locators
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome webdriver using webdriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the URL of the website to visit
website_url = 'https://mindrisers.com.np/contact-us'
# Open the website
driver.get(website_url)
driver.maximize_window()
time.sleep(5)

# Find the form elements by their XPath
first_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
phone_field = driver.find_element(By.XPATH, "//input[@placeholder='Phone']")
subject_field = driver.find_element(By.XPATH, "//input[@placeholder='Subject']")
queries_field = driver.find_element(By.XPATH, "//textarea[@placeholder='Queries']")


# Fill in the form fields with your data
first_name_field.send_keys('Jolly')
email_field.send_keys('jolly@gmail.com')
phone_field.send_keys('1234567890')
subject_field.send_keys('kdsfhjhsdh')
queries_field.send_keys('ckjdshciusdfcmsdhcviosdcvm,sdhvcshjkds')

# Find and click the submit button
submit_button = driver.find_element(By.XPATH,"//button[normalize-space()='Submit']")
submit_button.click()


# Extract and print the website title
website_title = driver.title
print(f"Website Title: {website_title}")

# Close the browser
driver.quit()
