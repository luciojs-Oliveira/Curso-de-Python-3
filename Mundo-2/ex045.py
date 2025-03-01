
'''
Exercício Python 45:
Crie um programa que faça o computador jogar Jokenpô com você.
'''


from random import randint
from time import sleep
itens = ("pedra", "Papel", "Tesoura")
computador = randint(0,2)
print(''' SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
#print("O Computador escolheu {}.".format(itens[computador]))
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!")
sleep(1)
print("=" * 20)
print("Computador jogou {}".format(itens[computador]))
print("jogador jogou {}.".format(itens[jogador]))
print("=" * 20)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: #3 computador jogou papel
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada inválida")

