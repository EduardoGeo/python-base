#!/usr/bin/env python

"""Calcula tabuada de 1 a 10
---Tabuada do 1---
    1 x 1 = 1
    1 x 2 = 2
...
------------------

---Tabuada do 2---
    2 x 1 = 2
    2 x 2 = 4
...
------------------
"""

__version__ = "0.1.0"
__author__ = "Eduardo Alves"

numeros = list(range(1, 11))
for n1 in numeros:
    print()
    print("{:-^18}".format(f" Tabuada do {n1} "))
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("-" * 18)
