# Created by illya at 9/30/2023
Feature: Simple Button Functionality

  Scenario: Click on "Click" button on Simple Button Page
    Given I navigate into the Simple Button Page
    When I click on "Click" button
    Then I can see the Submitted result