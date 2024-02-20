Feature: Freight Management

    Background:
        Given Launch the browser
        When Open the router app https://qa2-platform.navigo.global/apps/router/
        Then The login portal has been opened
        And Provide valid username and password
        And Click on the Login button
        Then Login is successful and dashboard is opened

#    Scenario: Create Freight if not available
#        When Click on Tab Freight Purchase
#        Then Create record if it is not available

    Scenario: Check Flight are available
        When Click on Tab Freight Purchase
        Then Verify the Flights are available
