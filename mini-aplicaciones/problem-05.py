#!/usr/bin/python3
"""
Practice 05: Game – Guess the number

Statement:
  Create a game where the system generates a random number and the player
  tries to guess the random number.

Analysis:
  * To create this game keep in mind the following data:
    * Hard 5 tries or lives
    * Intermediate 7 tries or lives
    * Easy 10 tries or lives
  * According to how you are trying the game should give you a clue if the
    number is bigger or smaller.
  * You also have to tell him how many lives you have left.
"""
import random


def game(lifes: int) -> None:
    random_number = random.randint(1, 100)
    chosen_number = None

    while random_number != chosen_number:
        chosen_number = int(input("Enter a number between 1 to 100: "))

        if random_number < chosen_number:
            print("Choose a smaller number")
            lifes -= 1
        elif random_number > chosen_number:
            print("Choose a biggest number")
            lifes -= 1

        if lifes == 0:
            print("Game Over")
            break

        print("You have {} lives left".format(lifes))

    if random_number == chosen_number:
        print("Congratulations you Won")


def main():
    while True:
        menu = """
        Guess the random number
        1- Easy level
        2- Intermediate level
        3- Hard level
        4- Go out

        ENTER AN OPTION: """

        option = input(menu)

        if option == '1':
            game(10)
        elif option == '2':
            game(7)
        elif option == '3':
            game(5)
        elif option == '4':
            print("Closing the game")
            break
        else:
            print("Wrong option, try again")

if __name__ == "__main__":
    main()
