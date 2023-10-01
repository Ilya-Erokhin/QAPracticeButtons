# Created by illya at 10/1/2023
Feature: Text Input Functionality

  Scenario: Type text into Input Simple Page
    Given I navigate to the Home Page
    When I click on Input Simple Page button
    And I can see the Input Field
    And I type "Ilia" into the field
    And Submit the result via Enter
    Then I can see the Submitted result with my text