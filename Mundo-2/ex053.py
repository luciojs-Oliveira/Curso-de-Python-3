
'''
Exercício Python 53:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
'''
#Exemplo 1
'''
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print("O inverso de: {} é: {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palindromo !")
else:
    print("A frase digitada não é um palindromo !")
'''

#Exemplo 2
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto [::-1]
print("O inverso de:{} é:{}".format(junto, inverso))
if inverso == junto:
    print("Temos um palindromo !")
else:
    print("A frase digitada não é um palindromo !")