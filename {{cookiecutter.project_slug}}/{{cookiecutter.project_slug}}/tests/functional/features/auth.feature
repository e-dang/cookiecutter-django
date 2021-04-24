Feature: Authentication flow
    As a user
    I want to be able to login, logout, reset and change my password
    So that I can use the application

    Scenario: A prospective user registers, confirms their email, and logs in
        Given I am on the register screen
        And I have valid registration information
        When I submit my information
        # And I confirm my email address
        # And I Go to the login screen
        # And I submit my credentials
        Then I am successfully logged in

