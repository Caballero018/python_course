#!/usr/bin/python3
"""
Practice 01: Calculate quotient and remainder

Statement:
  Find the quotient and remainder (remainder) of two integers.

Analysis:
  For the solution of this problem, the user is required to enter
  two integers and the system the respective calculation to perform the
  quotient and remainder
"""


print("Calculate quotient and remainder")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

quotient = a // b
remainder = a % b

print("The quotient is: {}\nThe residue is: {}".format(quotient, remainder))
