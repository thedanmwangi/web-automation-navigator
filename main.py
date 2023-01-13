import socket
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Check if there is an active network connection
try:
    socket.create_connection(("www.google.com", 80))
    print(">> Network connection active")
except OSError:
    print(">> No network connection")
    exit()

# Access the Huawei Router URL
url = "http://192.168.8.1/html/home.html"
print(f">> Accessing {url}")

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the home page
driver.get(url)

open_login_dialog_button = driver.find_element(By.ID, 'logout_span')
open_login_dialog_button.click()

# Find the email and password fields and enter the login credentials
driver.find_element(By.ID, "username").send_keys("my_username")
driver.find_element(By.ID, "password").send_keys("my_password")

# Find the login button and click it
login_button = driver.find_element(By.ID, 'pop_login')
login_button.click()

# Close the browser after 10 seconds
time.sleep(10)
driver.close()
