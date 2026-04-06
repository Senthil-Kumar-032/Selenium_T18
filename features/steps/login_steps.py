from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
import time

# valid test data
VALID_USER = "Enter valid emailid"
VALID_PASS = "Enter valid password"

@given("User opens Zen portal")
def step_open(context):
    # setup chrome with notifications disabled
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")

    context.driver = webdriver.Chrome(options=options)
    context.page = LoginPage(context.driver)

    # open site and handle popup
    context.page.open_url()
    context.page.close_popup_if_present()

@when("User enters valid credentials")
def step_valid_login(context):
    # login with correct credentials
    context.page.login(VALID_USER, VALID_PASS)
    context.page.close_popup_if_present()

@when("User enters invalid credentials")
def step_invalid_login(context):
    # login with wrong credentials
    context.page.login("senthil123@gmail.com", "Password.123")

@then("User should login successfully")
def step_success(context):
    # check login success by URL change
    assert context.driver.current_url != "https://v2.zenclass.in/login"

@then("Login should fail")
def step_fail(context):
    # check still on login page
    assert "login" in context.driver.current_url

@then("Input fields should be visible")
def step_validate_inputs(context):
    # verify email field is visible
    assert context.page.validate_input_fields()

@then("Login button should be enabled")
def step_validate_button(context):
    # verify login button is clickable
    assert context.page.validate_login_button()

@then("User logs out")
def step_logout(context):
    # perform logout and close browser
    context.page.logout()
    time.sleep(3)
    context.driver.quit()