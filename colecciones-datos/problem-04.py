#!/usr/bin/python3
"""
Enter 6 numbers in a list and get the largest and smallest number entered.
"""


number = []
print("Enter 6 numbers:")
for i in range(6):
    number.append(int(input("Number {}: ".format(i+1))))
number.sort()
print("The smallest number:", number[0])
print("The largest number:", number[-1])
