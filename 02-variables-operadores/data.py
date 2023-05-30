#!/usr/bin/python3
"""
Practice 02: Calculate sale price

Statement:
  Given the sale value of products, find the IGV (18%)
  and the sale price.

Analysis:
  For the solution of this problem, it is required that the user
  enter the sale value of the product and the system performs the
  respective calculation to find the IGV and the sale price, for
  this use the following expression.

  igv = vv * 0.18

  pv = vv + igv
"""


# Application Message
print("--- MAKE A SALE ---")

# Data entry
vv = float(input("Enter sale value: "))

# Operations
igv = vv * 0.18
pv = vv + igv

# Data output
print("="*25)
print("--- SALE INVOICE ---")
print("="*25)
print("Sale value:", vv)
print("IGV:", igv)
print("Sale price:", pv)
print("="*25)

