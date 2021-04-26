Feature: Authentication flow
    As a user
    I want to be able to login, logout, reset and change my password
    So that I can use the application

    Scenario: A prospective user registers, confirms their email, and logs in
        Given I am on the register page
        And I have valid registration information
        When I submit my information
        And I confirm my email address
        And I go to the login page
        And I submit my credentials
        Then I am successfully logged in
