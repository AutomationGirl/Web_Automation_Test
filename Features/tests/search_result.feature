Feature: search product and verify result

  Scenario: search product ,verify result and add to cart

    When I navigate to application url
    And Cancel popup if displayed
    And Search product shoes
    Then Verify searched category Footwear

    And Apply two filters on colour and brand
    And Verify filter Nike brand and Black colour are selected
    Then Verify result

    And Click on first product detail
    And Select size of product
    Then Click on buy now
    Then Should show login page





