#Crie um programa que leia o nome completo de uma pessoa e mostre :
#1 O nome com todas as letras maisculas .
#2 O nome com todas minúsculas.
#3 Quantas letras ao todo, Sem considerar espaços).
#4 Quantas letras tem o primeiro nome.


nome = str(input("Qual seu nome completo?")).strip()
print("Análisando seu nome...")
print("Seu nome em maiscula é: {}".format(nome.upper()))
print("Seu nome em minuscula é: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome) - nome.count(" ")))
#print("Seu primeiro nome tem {} letras.".format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))



