#!/usr/bin/python3

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

ls = [a, b, c]
for n in sorted(ls):
    print(n)
