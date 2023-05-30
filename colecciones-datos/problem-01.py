#!/usr/bin/python3
"""
  Practice 01: Restaurant discounts

  Statement:
    A restaurant offers a 10% discount for consumption of up to s/.
    100.00 and a 20% discount for larger consumption, for both cases
    a 19% tax is applied. Determine the amount of the discount,
    the tax and the amount to be paid.

  Analysis:
    to solve this problem, the user is required to enter the consumption
    and the system verifies and calculates the amount of the discount, the tax
    and the amount to be paid.
      * discount amount
      * taxes
      * import a payment
"""


print("Restaurant discounts")
consumption = int(input("Enter the consumption: "))
if consumption <= 100:
    discount = consumption / 10
if consumption > 100:
    discount = consumption / 20

d = consumption / 19
consumption -= d + discount

print("Discount value: ${:.2f}".format(discount + d))
print("Price value: ${:.2f}".format(consumption))
