#Faça um programa que leia números e mostre qual é o Maior e qual é o Menor.


a = int(input("Primeiro Valor: "))
b = int(input("Segundo Valor: "))
c = int(input("Terceiro Valor: "))
menor = a
if b < a and b < c:
    menor = b
if c < a or c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}: ".format(menor))
print("O maior valor digitado foi {}: ".format(maior))


