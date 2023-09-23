Feature: slider the bar element
  Scenario: slider the bar element to 100
    Given the user Navigate to the URL https://qavbox.github.io/demo/dragndrop/
    When he move the slider bar
    Then the value 100 will be displayed