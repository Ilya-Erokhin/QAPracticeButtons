# Created by illya at 9/30/2023
Feature: Simple Button Functionality

  Scenario: Navigate from Home Page to Simple Button Page and click on it
    Given I navigate to the Home Page
    When I click on Simple Page button
    When I click on "Click" button
    Then I can see the Submitted result