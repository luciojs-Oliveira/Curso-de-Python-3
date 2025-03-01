


# Exercicios 36 - Aprovando Empréstimos
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''


casa = float(input("Valor da casa : R$ "))
salário = float(input("Sálario do comprador: R$"))
anos = int(input("Quantos anos de Financiamento? "))
prestação = casa / (anos * 12)
minimo = salário * 30 /100
print( "Para pagar uma casa de {:.2f} em {} anos ".format(casa, anos))
print("A prestação será de {:.2f}".format(prestação))
"Para pagar uma casa de {:.2f} em {} anos "
if prestação <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO !")
