#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e a último nome separadamente.
#EX: Ana Maria de Souza
#primeiro = Ana
#Último = Souza

n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é :{}".format(nome[0]))
print("Seu último nome é {}".format(nome[len(nome)-1]))