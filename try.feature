Feature: Factorial Calculation

  @Jiraticket
  @positivetest
  Scenario Outline: Calculate factorial of a positive number
    Given UI: I am on factorial calculator page
    And   UI: Input an integer 5
    And   UI: Click Calculate
    Then  Verify the factorial of <value> is <result>
    Examples:
      |value|result|
      |5    |120   |

  @Jiraticket
  @paramtertest
  Scenario Outline: Calculate factoiral of a decimal number
    Given UI: I am on factorial calculator page
    And   UI: Input an integer <positive_int_value>
    And   UI: Click Calculate
    Then  UI: Verify the result is <result>
    Examples:
      | positive_int_value  | result |
      | 2.5                 | 120    |
      | 10.5                | 1      |
      | 100.5               | 1      |


  @Jiraticket
  @paramtertest
  Scenario Outline: Calculate factorial of a floating number
    Given UI: I am on factorial calculator page
    And   UI: Input an integer <positive_int_value>
    And   UI: Click Calculate
    Then  UI: Verify the result is <result>
    Examples:
      | positive_int_value | result |
      | 5                  | 120    |
      | 0                  | 1      |
      | 1                  | 1      |

  @Jiraticket
  @negativetest
  Scenario Outline: Calculate factorial of a negative number
    Given UI: I am on factorial calculator page
    And   UI: Input an integer <positive_int_value>
    And   UI: Click Calculate
    Then  UI: Verify the result is <result>
    Examples:
      | positive_int_value | result |
      | 5                  | 120    |
      | 0                  | 1      |
      | 1                  | 1      |

  @Jiraticket
  @negativetest
  Scenario Outline: Calculate factoiral of a big digit number
    Given UI: I am on factorial calculator page
    And   UI: Input an integer <positive_int_value>
    And   UI: Click Calculate
    Then  UI: Verify the result is <result>
    Examples:
      | positive_int_value | result |
      | 5                  | 120    |
      | 0                  | 1      |
      | 1                  | 1      |