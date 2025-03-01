#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usúario tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usúario venceu ou perdeu.






from random import randint
from time import sleep
computador = randint(0,10)# Faz o computador "pensar".
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10 . tente adivinhar...")
print("-=-" * 20)
jogador  = int(input("Em que número eu pensei? ")) #jogador tenta advinhar...
print("Processando ...")
sleep(3)
if jogador == computador:
    print("Parabéns ! você conseguiu me vencer! ")
else:
    print("Ganhei ! Eu pensei no número {} e não no {} !" .format(computador, jogador))