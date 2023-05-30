#!/usr/bin/python3
"""
  Practice 02: Restaurant discounts Part 02

  Statement:
    due to the excellent results, the restaurant decides to expand its offers
    according to the following scale of consumption, see the table. Determine
    the amount of the discount, the amount of the tax and the amount to be
    paid.

    * Consumption (S/.) Discount (%)
      * Up to 100 10
      * Greater than 100 20
      * Greater than 200 30

  Analysis:
    for the solution of this problem, the user is required to enter the
    consumption and the system verifies and calculates the amount of the
    discount, the tax and the amount to be paid.
"""

print("Restaurant discounts")
consumption = int(input("Enter the consumption: $"))

if consumption >= 0:
    if consumption > 100 and consumption <= 200:
        discount = consumption / 20
    elif consumption > 200:
        discount = consumption / 30
    else:
        discount = consumption / 10

    consumption -= discount
    print("Discount value: ${:.2f}".format(discount))
    print("Price value: ${:.2f}".format(consumption))
