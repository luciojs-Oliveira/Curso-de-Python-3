#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, culcule e mostre o comprimento da hipotenusa.
"""exemplo: 1
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenua vai medir {:.2f}".format(hi))"""


#exemplo: 2
from math import hypot
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = hypot(co , ca)
print("A hipotenusa vai medir {:.2f} ".format(hi))
