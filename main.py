import time
from datetime import datetime

import requests

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Huawei Router URL to be accessed
baseUrl = "http://192.168.8.1/"
homeUrlExt = "html/home.html"
ussdUrlExt = "html/ussd.html"


def activeNetworkConnection():
    # Check if there is an active network connection
    try:
        req = requests.get("https://google.com")
        req.raise_for_status()
        return True

    except:
        return False


def accessHuaweiRouterUrlOnBrowser():
    # Access the Huawei Router URL on Firefox
    driver = webdriver.Firefox()
    print(f">> Accessing {baseUrl + homeUrlExt}")
    driver.get(baseUrl + homeUrlExt)

    # Open the Login dialog box
    open_login_dialog_button = driver.find_element(By.ID, 'logout_span')
    open_login_dialog_button.click()
    time.sleep(2)

    # Find the email and password fields and enter the login credentials
    driver.find_element(By.ID, "username").send_keys("my_username")
    driver.find_element(By.ID, "password").send_keys("my_password")

    # Find the login button and click it
    login_button = driver.find_element(By.ID, 'pop_login')
    login_button.click()

    time.sleep(1)
    # Find the USSD tab and click it
    ussd_button = driver.find_element(By.ID, 'ussd')
    ussd_button.send_keys(Keys.ENTER)

    time.sleep(1)
    # Find the USSD query input and enter the USSD code
    # driver.find_element(By.ID, "general_command_select_input").send_keys("*544#")

    time.sleep(1)
    # Find the Send button and click it
    send_ussd_button = driver.find_element(By.ID, 'general_btn')
    send_ussd_button.click()

    time.sleep(1)
    # Logout the automated process
    driver.find_element(By.ID, 'logout_span').click()
    driver.find_element(By.ID, 'pop_confirm').click()

    # Close the browser after 10 seconds
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    # dd/mm/YY H:M:S
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if activeNetworkConnection():
        print(">> Network connection active")
        print(">> Process started at " + dt_string)
        accessHuaweiRouterUrlOnBrowser()
    else:
        print(">> No network connection")
        print(">> Process terminated at " + dt_string)
        exit()

