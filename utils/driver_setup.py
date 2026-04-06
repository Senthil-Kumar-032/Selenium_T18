from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverSetup:

    def get_driver(self):
        options = Options()
        options.add_argument("--disable-notifications")  # disable popup
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver