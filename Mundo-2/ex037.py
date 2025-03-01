


# Exercicios 37 - Conversor de Bases númericas.

'''0X para hexadecimal, 0C para Octal, bin para Binário'''

'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input("Digite um número: "))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input("Sua opção :"))
if opção == 1:
    print("{} convertido para BINÁRIO é igual {}".format(num, bin(num)[2:]))
elif opção == 2:                                                                  #elif = senão se
    print("{} convertido para OCTAL é igual {}".format(num, oct(num)[2:]))        #fatiamento [:2] da posição 2 até o final
elif opção == 3:
    print("{} convertido para HEXADECIMAL é igual {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida, Tente novamnete !")



