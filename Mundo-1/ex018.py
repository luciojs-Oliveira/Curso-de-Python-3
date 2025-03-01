#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

#Exemplo: 01
"""import math
ângulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(ângulo))
print("O ângulo de {} tem o seno de {:.2f} ".format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print("O ângulo de {} tem o cosseno de {:.2f}".format(ângulo, cosseno))
tangente = math.tan(math.radians((ângulo)))
print("O ângulo de {} tem a Tangente de {:.2f}".format(ângulo,tangente))"""

from math import radians,sin, cos, tan
ângulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(ângulo))
print("O ângulo de {} tem o seno de {:.2f}".format(ângulo,seno))
cosseno = cos(radians(ângulo))
print("O ângulo de {} tem o cosseno de {:.2f}".format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print("O ângulo de {} tem a tangente de {:.2f}".format(ângulo, tangente))