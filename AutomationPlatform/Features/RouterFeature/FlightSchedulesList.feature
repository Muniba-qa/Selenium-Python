Feature: Flight Schedules List

  Background:
    Given Launch the browser
    When Open the router app https://qa2-platform.navigo.global/apps/router/
    Then The login portal has been opened
    And Provide valid username and password
    And Click on the Login button
    Then Login is successful and dashboard is opened

  Scenario: Schedule the flight
    Then Click on Tabs Flight Schedule List
    Then Create the New Flight Schedule
    Then Verify Flight Created or not
    Then Close the browser


