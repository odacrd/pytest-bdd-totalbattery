Feature: Add items to the cart

  Background: User goes to Total Battery website
    Given the user has navigated to the Total Battery Home page

  Scenario Outline: User adds two items to the cart
    Given the user has navigated to the Total Battery online store
    And the shopping cart is empty

    When the user picks 'Small and Specialty Batteries - Drones'
    And first item added is <item1>
    And the user navigates back one page
    And next item added is <item2>
    Then the actual total equals the calculated total and the <expected_total>

    When the user proceeds to checkout
    Then the checkout subtotal equals the <expected_total>

    When user enters all required data except phone number
    Then an Error Message is displayed

    When user enters missing phone number
    Then 'Continue Payment' button is displayed

    When 'Continue Payment' button is clicked
    Then the 'Pay' amount is <pay_amount>


    Examples:
      | item1                    | item2                    | expected_total | pay_amount |
      | DJI Drones - CS-DJP300RC | SYMA Drones - CS-LT124RX | 56.12 | 63.42        |
