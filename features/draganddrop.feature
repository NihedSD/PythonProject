Feature: drag and drop an element
  Scenario: drag an d drop an element in the square
    Given the user Navigate to the URL https://qavbox.github.io/demo/dragndrop/
    When he drag and drop the grey square in the blue square
    Then he sees a messge "Dropped!"