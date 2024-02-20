Feature: Freight Management

    Background:
        Given Launch the browser
        When Open the router app https://qa2-platform.navigo.global/apps/router/
        Then The login portal has been opened
        And Provide valid username and password
        And Click on the Login button
        Then Login is successful and dashboard is opened

    Scenario: Verify Status DropDown is Visible
        Then Click on Tab Freight Management
        When Freight Management records available
        Then Click on edit btn
        Then Verify the Select dropdown
        Then Close the browser

    Scenario: Flight schedule remains after cancel button
        Then Click on Tab Freight Management
        When Freight Management records available
        Then Click on edit btn
        Then Click on cancel btn
        Then Verify the Freight Management Tab
        Then Close the browser


    Scenario Outline: Save the Status
        Then Click on Tab Freight Management
        Then Get the old status
        Then Click on edit btn
        Then Click on status
        Then Click on save btn
        Then Check the Status Changed or not "<Status>"
        Then Close the browser
        Examples:
            | Status |
            | Save   |

    Scenario Outline: Cancel the Status
        Then Click on Tab Freight Management
        Then Get the old status
        Then Click on edit btn
        Then Click on status
        Then Click on cancel btn
        Then Check the Status Changed or not "<Status>"
        Then Close the browser
        Examples:
            | Status |
            | Cancel |

    Scenario: Freight Management Tab
        Then Click on Tab Freight Management
        Then Verify the Freight Management Tab
        Then Close the browser

    Scenario Outline: Access to Freight Management Tab
        And Provide the Credentials "<username>" and "<password>"
        And Click on the Login button
        Then Check the Freight Management Tab
        Then Close the browser
        Examples:
            | password | username                  |
            | 1234     | automation@navigo-inc.com |

    Scenario: Verify Freight Table View
        Then Click on Tab Freight Management
        Then Verify the Freight Table columns
        Then Close the browser


    Scenario: Open the Contact Info
        Then Click on Tab Freight Management
        Then Click on Contact Info btn
        Then Close the browser

    Scenario: Select Available Flight
        Then Click on Tab Freight Purchases
        Then Click on the Purchase new Freight
        Then Select Available Flight
        Then Close the browser

    Scenario: View the Contact Info
        Then Click on Tab Freight Management
        Then Click on Contact Info btn
        Then Is Contact info visible
        Then Click on cancel btn
        Then Close the browser

    Scenario: View records as a table format
        Then Click on Tab Freight Management
        Then verify it is in table format
        Then Close the browser
