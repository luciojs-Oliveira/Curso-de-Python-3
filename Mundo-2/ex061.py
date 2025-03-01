'''
Exercício Python 61:
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''




print("Gerador de PA")
print("-=-" * 5)
primeiro = int(input("Primeiro termo: "))
print("-=-" * 5)
razão = int(input("Razão de PA: "))
print("-=-" * 5)
termo = primeiro
cont = 1
while cont <= 10:
    print("{} ->".format(termo), end=" ")
    termo += razão
    cont += 1
print("Fim")

