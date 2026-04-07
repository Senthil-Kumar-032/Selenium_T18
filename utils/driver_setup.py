from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverSetup:

    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--disable-notifications")  # disable browser notifications
        options.add_argument("--start-maximized")        # open browser in full screen

        driver = webdriver.Chrome(options=options)      # launch Chrome browser
        driver.implicitly_wait(10)                       # apply implicit wait
        return driver                                   # return driver instance