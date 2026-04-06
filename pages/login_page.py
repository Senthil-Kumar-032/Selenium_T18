from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver        # store driver instance

        # locators for elements
        self.email = (By.XPATH, "//input[@placeholder='Enter your mail']")
        self.password = (By.XPATH, "//input[@placeholder='Enter your password ']")
        self.login_btn = (By.XPATH, "//button[contains(text(),'Sign in')]")

        self.profile_icon = (By.ID, "profile-click-icon")
        self.logout_btn = (By.XPATH, "//div[text()='Log out']")
        self.close_popup = (By.CLASS_NAME, "custom-close-button")

    def open_url(self):
        # open website and setup browser
        self.driver.get("https://v2.zenclass.in/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close_popup_if_present(self):
        # close popup if it appears
        try:
            self.driver.find_element(*self.close_popup).click()
        except NoSuchElementException:
            pass        # ignore if popup not found

    def enter_email(self, email):
        # enter email in input field
        self.driver.find_element(*self.email).clear()
        self.driver.find_element(*self.email).send_keys(email)

    def enter_password(self, password):
        # enter password in input field
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        # click login button
        self.driver.find_element(*self.login_btn).click()

    def login(self, email, password):
        # perform complete login action
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        time.sleep(5)  # wait for login

    def validate_input_fields(self):
        # check if email field is visible
        return self.driver.find_element(*self.email).is_displayed()

    def validate_login_button(self):
        # check if login button is enabled
        return self.driver.find_element(*self.login_btn).is_enabled()

    def logout(self):
        # logout from application
        time.sleep(3)
        self.driver.find_element(*self.profile_icon).click()
        self.driver.find_element(*self.logout_btn).click()