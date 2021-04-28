Feature: Authentication flow
    As a user
    I want to be able to login, logout, reset and change my password
    So that I can use the application

    Scenario: A prospective user registers, confirms their email, and logs in
        Given I am an unverified user
        And I am on the register page
        And I have valid registration information
        When I submit my information
        And I confirm my email address
        And I go to the login page
        And I submit my credentials
        Then I am successfully logged in

    Scenario: A verified user logs in, changes their password, logs out, and logs back in with their new password
        Given I am a verified user
        And I am on the login page
        And I have valid login credentials
        When I submit my credentials
        And I go to the user settings page
        And I change my password
        And I logout
        And I go to the login page
        And I submit my new credentials
        Then I am successfully logged in

    Scenario: A verified user forgot their password, resets it, and logs in using their new password
        Given I am a verified user
        And I am on the password reset page
        When I submit a request to reset my password
        And I follow the link to reset my password
        And I submit my new password
        And I go to the login page
        And I submit my new credentials
        Then I am successfully logged in
