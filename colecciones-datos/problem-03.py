#!/usr/bin/python3
"""
  Practice 03: Save odd and even results

  Statement:
    Create 2 lists and a tuple that will have numbers from 1 to 9. The
    first list will be called even and the second odd, both will be empty.
    Then multiply each of the numbers in the tuple by a random number between
    1 and 100, if the result is even, save that number in the even list and if
    it is odd in the odd list. Displays by console: -the multiplication that
    occurs along with its result in the format 2 x 3 = 6 and the list of even
    and odd
"""
import random


odd = []
peers = []
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for number in numbers:
    number *= random.randint(1, 100)
    if number % 2 == 0:
        peers.append(number)
    else:
        odd.append(number)

print("List the peers: {}".format(peers))
print("List the odd: {}".format(odd))
