from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import os
os.environ["webdriver.chrome.driver"] = 'C:\\webdriver\\chromedriver.exe'

# Create the WebDriver without specifying executable_path
driver = webdriver.Chrome()

# Navigate to the Threads login page
driver.get('https://www.threads.net/login')
driver.maximize_window()
# Find and fill in the login form
username_input = driver.find_element(By.XPATH, '//input[@placeholder="Username, phone or email"]')
password_input = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')

username_input.send_keys('tafise3516@wlmycn.com')
password_input.send_keys(')5vKhRXp!c7<mx.')

# Submit the form
password_input.send_keys(Keys.ENTER)

# Wait for the login to complete (you may need to adjust the wait time)
time.sleep(5)

# Find the first tweet in the timeline and like it
like_button = driver.find_element(By.XPATH, '//*[@aria-label="Like"]')
like_button.click()

time.sleep(5)

try:
    element = driver.find_element(By.XPATH, '//*[@aria-label="Unlike"]')
    print('Test Passed: Tweet was liked successfully!')
except NoSuchElementException:
    print('Test Failed: Tweet was liked successfully!')
# Close the browser
driver.quit()
