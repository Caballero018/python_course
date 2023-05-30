#!/usr/bin/python3
"""
Practice 03: Password generator

Statement:
  Create a system that generates a random password

Analysis:
  Solving this problem requires lists, uppercase lists, lowercase lists,
  number lists, and symbol lists, and then building a random password by
  pulling characters from these lists.
"""
import random


def password_generator() -> str:
    alphabet = [chr(a) for a in range(97, 122 + 1)] +\
        [chr(a) for a in range(65, 90 + 1)]
    numbers = [str(n) for n in range(1, 10)] + [str(0)]
    symbols = ['#', "$", "%", "&"]
    characaters = alphabet + numbers + symbols
    password = []

    for _ in range(15):
        # Take a random character from a list
        random_number = random.choice(characaters)

        password.append(random_number)

    return "".join(password)


def main():
    password = password_generator()
    print("Your new password is: {}".format(password))


if __name__ == "__main__":
    main()
