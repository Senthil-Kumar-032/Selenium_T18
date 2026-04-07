# Behave step keywords
from behave import given, when, then
from pages.login_page import LoginPage
from utils.driver_setup import DriverSetup
import json

# Load test data from JSON file
def load_data():
    with open("test_data.json") as f:
        return json.load(f)

data = load_data()  # store data globally

# Open browser and load website
@given("User opens Zen portal")
def step_open(context):
    context.driver = DriverSetup().get_driver()   # start browser
    context.page = LoginPage(context.driver)      # create page object

    context.page.open_url()                       # open site
    context.page.close_popup_if_present()         # close popup if any

# Login with valid credentials
@when("User enters valid credentials")
def step_valid_login(context):
    user = data["valid_user"]                     # get valid user
    context.page.login(user["username"], user["password"])
    context.page.close_popup_if_present()         # close popup again if needed

# Login with invalid credentials
@when("User enters invalid credentials")
def step_invalid_login(context):
    user = data["invalid_user"]                   # get invalid user
    context.page.login(user["username"], user["password"])

# Check login success
@then("User should login successfully")
def step_success(context):
    assert context.driver.current_url != "https://v2.zenclass.in/login"

# Check login failure
@then("Login should fail")
def step_fail(context):
    assert "login" in context.driver.current_url

# Check input fields visible
@then("Input fields should be visible")
def step_validate_inputs(context):
    assert context.page.validate_input_fields()

# Check login button enabled
@then("Login button should be enabled")
def step_validate_button(context):
    assert context.page.validate_login_button()

# Logout step
@then("User logs out")
def step_logout(context):
    context.page.logout()