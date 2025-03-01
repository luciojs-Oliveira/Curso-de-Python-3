#Aula 12 Condições Aninhadas



"""Exemplo de estrutura condicional simples
nome = str(input("Qual é o seu nome? "))
if nome == "Luiza" :
    print("Que no nome lindo! ")
print("Tenha uma boa noite ,{}! ".format(nome))
"""

#'Exemplo de estrutura condiciona composta
"""
nome = str(input("Qual o seu nome? "))
if nome == "Luiza":
    print("Que nome lindo! ")
else:
    print("Seu nome é bem Normal! ")
print("Tenha uma boa noite, {}".format(nome))
"""
'''
#Exemplo de estrutura de condicional Aninhada
nome = str(input("Qual o seu nome?"))
if nome == "Luiza" :
    print("Que nome lindo ! ")
elif nome == "Maria" or nome == "Marisa" or nome == "Maria Eduarda":
    print("Seu nome é bem popular no Brasil. ")
else:
    print("Seu nome é bem Normal. ")
print("Tenha um bom dia , {}!".format(nome))
'''

'''
#Exemplo de estrutura  condicional Aninhada
nome = str(input("Qual o seu nome?"))
if nome == "Luiza" :
    print("Que nome lindo ! ")
elif nome == "Maria" or nome == "Marisa" or nome == "Maria Eduarda":
    print("Seu nome é bem popular no Brasil. ")
elif  nome  in "Ana Claudia Cleide Juliana Gisele":
    print("Que nome legal você tem !")
else:
    print("Seu nome é bem Normal. ")
print("Tenha um bom dia , {}!".format(nome))
'''













