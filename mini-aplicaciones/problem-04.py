#!/usr/bin/python3
"""
Practice 04: Currency Converter

Statement:
  Create a system that converts from national currency to dollars, for example,
  from Peruvian soles to dollars, Mexican pesos to dollars, Colombian pesos to
  dollars.

Analysis:
  * To solve this problem, the user is required to enter the number of national
    currencies and then perform the conversion.
  * For this system you must make a navigation menu to select what type of cu-
    rrency the conversion will be used for and also to close the program, the
    system should not be closed if you do not want it.
"""


def converter(dollar_value, country):
    amount_coins = float(input("Enter amount of {}: ".format(country)))

    dollars = amount_coins / dollar_value
    dollars = round(dollars, 2)
    print("You have ${} dollars".format(dollars))


def main():
    while True:
        menu = """
        1- Soles peruanos a Dolares
        2- Pesos Mexicanos a dolares
        3- Pesos Colombianos a dolares
        4- Salir
        Ingrese una Opción:
        """
        option = input(menu)

        if option == '1':
          converter(3.61, "soles peruanos")
        elif option == '2':
          converter(20, 'pesos Mexicanos')
        elif option == '3':
          converter(4470, "pesos colombianos")
        elif option == '4':
          print("Closed currency Converter")
          break
        else:
           print("Incorrect option")
           print("Re-enter the correct option")
       
        


if __name__ == "__main__":
    main()