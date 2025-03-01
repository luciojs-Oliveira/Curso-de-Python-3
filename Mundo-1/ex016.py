#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção interira.
#Ex: Digite um número :6127 O número 6.127 tem a parte Inteira 6.

#exemplo: 1
"""import math
num = float(input("Digite um valor:"))
print("O valor digitado foi {} e a sua porção inteira é {} ".format(num, math.trunc(num)))

#exemplo: 2
from math import trunc
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))"""

#exemplo: 3
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, int(num)))