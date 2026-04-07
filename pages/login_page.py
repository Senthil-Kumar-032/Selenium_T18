# Imports for Selenium actions and waits
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Login page class
class LoginPage:

    def __init__(self, driver):
        self.driver = driver  # store driver

        # Locators
        self.email = (By.XPATH, "//input[@placeholder='Enter your mail']")  # email field
        self.password = (By.XPATH, "//input[@type='password']")  # password field
        self.login_btn = (By.XPATH, "//button[contains(text(),'Sign in')]")  # login button

        self.profile_icon = (By.ID, "profile-click-icon")  # profile icon after login
        self.logout_btn = (By.XPATH, "//div[text()='Log out']")  # logout option
        self.close_popup = (By.CLASS_NAME, "custom-close-button")  # popup close

    # Open login page
    def open_url(self):
        self.driver.get("https://v2.zenclass.in/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Close popup if it shows up
    def close_popup_if_present(self):
        try:
            self.driver.find_element(*self.close_popup).click()
        except NoSuchElementException:
            pass  # ignore if no popup

    # Type email
    def enter_email(self, email):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email)
        )
        element.clear()
        element.send_keys(email)

    # Type password
    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password)
        )
        element.clear()
        element.send_keys(password)

    # Click login
    def click_login(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_btn)
        )
        element.click()

    # Full login flow
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        time.sleep(3)  # wait for page load

    # Check email field is visible
    def validate_input_fields(self):
        return self.driver.find_element(*self.email).is_displayed()

    # Check login button is enabled
    def validate_login_button(self):
        return self.driver.find_element(*self.login_btn).is_enabled()

    # Check login success (URL changes)
    def is_login_successful(self):
        return "dashboard" in self.driver.current_url

    # Check login failed (still on login page)
    def is_login_failed(self):
        return "login" in self.driver.current_url

    # Logout from app
    def logout(self):
        time.sleep(3)
        self.driver.find_element(*self.profile_icon).click()
        self.driver.find_element(*self.logout_btn).click()