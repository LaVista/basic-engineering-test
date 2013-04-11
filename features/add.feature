Feature: Add two numbers
  In order to set an example
  As a lazy Product Owner
  Let show a happy path addition

  Scenario: One plus one is two
    Given I go to "http://localhost:8080/calc"
    When I fill in "value 1" with "1"
    And I fill in "value 2" with "1"
    And I select "+" from "operator"
    And I press "Submit"
    Then I should see "1 + 1 = 2"
