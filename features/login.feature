Feature: Zen Portal Login

  Scenario: Successful Login
    Given User opens Zen portal
    When User enters valid credentials
    Then User should login successfully

  Scenario: Invalid Login
    Given User opens Zen portal
    When User enters invalid credentials
    Then Login should fail

  Scenario: UI Validation
    Given User opens Zen portal
    Then Input fields should be visible
    And Login button should be enabled

  Scenario: Logout
    Given User opens Zen portal
    When User enters valid credentials
    Then User logs out