
'''
Exercício Python 48:
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''



soma = 0           #Acumulador
cont = 0           #Acumulador
for c in range (1, 501, 2):             #for = laço de repetição
    if c % 3 == 0:
        soma += c
        cont += 1
print(" A soma de todos os {} valores solicitados é {}".format(cont, soma))


'''
for c in range (1, 501, 2):            #Contador de  1 até  500 de 2em 2 impar
    print(c, end= ' ')                 #O uso de end= ' ' <-espaço vazio serve para mostrar o número na horizontal
'''
'''
for c in range (2, 501, 2):            #contador de 1 até 500 de 2 em 2 par
    print(c)
'''