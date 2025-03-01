#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

#Verifica letras minusculas dentro de uma frase.
#nome = str(input("Qual é o seu nome comleto? ")).strip()
#print("Seu nome tem Silva? {}".format("silva" in nome.upper()))

#Verifica letras Maiusculas dentro de uma frase.
nome = str(input("Qual é o seu nome comleto? ")).strip()
print("Seu nome tem Silva? {}".format("silva" in nome.lower()))