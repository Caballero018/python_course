#!/usr/bin/python3
"""
Practice 02: Primality

Statement:
  Create a system that detects if a number is prime or not

Analysis:
  * To solve this problem, the user is required to enter a number on the
    keyboard and the system detects if it is prime or not.
  * A prime number is one that can be divided only twice by 1 and itself.
"""


def prime_numbers(number):
    count = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue

        """
        Verify that the division with the numbers up to the entered
        number is equal to zero
        """
        if number % i == 0:
            count += 1

    if count == 0:
        return True
    return False


def main():
    number = int(input("Enter a number: "))
    if prime_numbers(number):
        print("Is prime")
        return
    print("Not prime")


if __name__ == "__main__":
    main()
