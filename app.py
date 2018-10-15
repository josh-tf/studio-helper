import os
import time
import atexit
from setup import *
from functions import *
from selenium.webdriver.common.by import By

envStudio = os.environ['envStudio']

def handleExit():
    print("Cleaning up resources..")
    browser.quit()
    display.stop()

def quitwithErr():
    print("An error has occurred.. exiting")
    quit()

# register our handleExit function above to do it nicely
atexit.register(handleExit)

# for debugging lets add a timer
start_time = time.time()

# create our display and browser window
display = createDisplay()
browser = createBrowser()

# navigate to our main front page
browser.get('https://clients.mindbodyonline.com/classic/mainclass?studioid=' + envStudio)

# login to our browser, exit if not successful
if not loginBrowser(browser): quitwithErr()

# navigate to our schedules page
browser.get('https://clients.mindbodyonline.com/ASP/my_sch.asp')

# confirm we are still logged in
if not checkSession(browser): quitwithErr()

# Content scraping
#browser.execute_script("return something")

data = []
for tr in browser.find_elements_by_xpath('//table[@id="mySchTable"]//tr'):
    tds = tr.find_elements_by_tag_name('td')
    if tds:
        data.append([td.text for td in tds])
print(data)

# take a screenshot (for debugging)
browser.get_screenshot_as_file("capture.png")

# print to stout the page title and the dev timer result
print (browser.title)
print(time.time() - start_time)