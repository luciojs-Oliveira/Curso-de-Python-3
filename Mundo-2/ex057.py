


'''
Exercício Python 57:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = str(input("Dgite o seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor , Informe seu sexo :  ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))
