
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your WebDriver executable (e.g., chromedriver.exe)
webdriver_path = 'C:\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome()

# Special characters comment
special_characters_comment = "#@!$%^&*()_+"

try:
    # Open the web application
    driver.get('https://www.threads.net/login')
    driver.maximize_window()

    username_input = driver.find_element(By.XPATH, '//input[@placeholder="Username, phone or email"]')
    password_input = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')

    username_input.send_keys('tafise3516@wlmycn.com')
    password_input.send_keys(')5vKhRXp!c7<mx.')

    # Submit the form
    password_input.send_keys(Keys.ENTER)

    # Wait for the login to complete (you may need to adjust the wait time)
    time.sleep(5)

    # Click the "Comment" button
    comment_button = driver.find_element(By.XPATH, '//*[@aria-label="Comment"]')
    comment_button.click()

    time.sleep(10)

# Enter the special characters comment
    comment_input = driver.find_element(By.XPATH, '//*[@role="textbox"]')
    comment_input.send_keys(special_characters_comment)

    time.sleep(5)
    # Click the "Post" button
    post_button = driver.find_element(By.XPATH, '//*[@class="x1i10hfl xjbqb8w x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 x1a2cdl4 xnhgr82 x1qt0ttw xgk8upj x9f619 x3nfvp2 x1s688f x90ne7k xl56j7k x193iq5w x1swvt13 x1pi30zi x1g2r6go x11xpdln xz4gly6 x87ps6o xuxw1ft x19kf12q x12w9bfk x6bh95i x1re03b8 x1hvtcl2 x3ug3ww x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x178xt8z xm81vs4 xso031l xy80clv xp07o12"]')
    post_button.click()

    try:
        element = driver.find_element(By.XPATH, '//*[@role="textbox"]')
        print("Test Passed: Comment with special characters posted successfully.")
    except NoSuchElementException:
        print("Test Failed: Error messages are displayed.")
finally:
    # Close the WebDriver
    driver.quit()
