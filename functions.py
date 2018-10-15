from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

envUsername = os.environ['envUsername']
envPassword = os.environ['envPassword']

global delay # global var for timeout, adjust for latency
delay = 3 # seconds

# fill out login form and submit it
def loginBrowser(browser):
    browser.find_element_by_name("requiredtxtUserName").send_keys(envUsername)
    browser.find_element_by_name("requiredtxtPassword").send_keys(envPassword)
    browser.find_element_by_id("btnLogin").send_keys(Keys.ENTER)

    return checkSession(browser)

def checkSession(browser):
    try:
        logoutBtn = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, "btnLogout")))
        return True # success
    except TimeoutException:
        return False # some error (time out)
