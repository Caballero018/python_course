#!/usr/bin/env python3
"""
Application 01: Fibonacci Sequence

Statement:
    Create a module that generates a Fibonacci sequence, within this
    module create two functions:

Analysis:
    * The first function that generates the Fibonacci sequence with numbers
    * The second function that returns a list of Fibonacci sequences
"""


def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()

def fibo2(n):
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = a, a + b

    return result
