'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

#para transformar a variavel núm em uma tupla basta adicionar paraneteses no inicio e no final.

núm = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o ultimo número: ")),)
print(f"Você digitou os valores {núm}")
print(f"O valor 9 apreceu {núm.count(9)} vezes")
if 3 in núm:
    print(f"O Valor 3 apareceu na {núm.index(3)+1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("Os valores pares digitados foram", end=" ")
for n in núm:
    if n % 2 == 0:
        print(n, end=" ")



