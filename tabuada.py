#!/usr/bin/env python3

"""Calcula tabuada de 1 a 10
Tabuada do 1
1
2
3
...
------------
Tabuada do 2
2
4
6
...
"""

__version__ = "0.1.0"
__author__ = "Eduardo Alves"


numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do: ", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("--------------")
