
'''
Exercício Python 46:
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''


from time import sleep          # Biblioteca time
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)                    # Função sleep
print("BUUM BUM POWW!!!")       #fogos de artificios
