#Crie um programa que leia um número interio e mostre na tela se ele é Par ou Impar.



número  = int(input("me diga um número qualquer: "))
resultado = número % 2
if resultado == 0:
    print("O número {}: é PAR".format(número))
else:
    print("O número {}: é IMPAR".format(número))