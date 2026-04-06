Feature: Zen Portal Login

  Scenario: Successful Login
    Given User opens Zen portal
    When User enters valid credentials
    Then User should login successfully
    And User logs out

  Scenario: Unsuccessful Login
    Given User opens Zen portal
    When User enters invalid credentials
    Then Login should fail

  Scenario: Validate Inputs
    Given User opens Zen portal
    Then Input fields should be visible

  Scenario: Validate Submit Button
    Given User opens Zen portal
    Then Login button should be enabled