from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# create a virtual display to run chrome in
def createDisplay():
    display = Display(visible=0, size=(800, 800))
    display.start()
    return display

def createBrowser():
    # define our chrome driver options and preferences
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})

    # create our selenium web driver
    return webdriver.Chrome(chrome_options=chrome_options)