import allure
from allure_commons.types import AttachmentType

# Screenshot on failure
def after_step(context, step):
    if step.status == "failed":
        if context.driver:
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG
            )

# Close browser after each scenario
def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()