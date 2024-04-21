from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website_url ='https://demoqa.com/alerts'

driver.get(website_url)

driver.maximize_window()

click_me= driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))

click_me.click()

time.sleep(4)

alert = driver.switch_to.alert

alert.accept()

print("Congrats")
driver.close()