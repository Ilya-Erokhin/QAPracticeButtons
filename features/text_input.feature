# Created by illya at 10/1/2023
Feature: Text Input Functionality

  Scenario: Type text into "Text Input Page"
    Given I navigate into the Text Input Page
    When I can see the Input Field
    And I type "Ilia" into the field
    And Submit the result via Enter
    Then I can see the Submitted result with my text