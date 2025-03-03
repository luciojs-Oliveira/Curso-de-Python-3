'''
Exercício Python 084:
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

temp = []
princ = []

while True:
    temp.append(str(input("nome:")))
    temp.append(float(input('peso:')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer contiuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end=' ')
for p in princ:
    if p[1] == men:
        print(f"[{p[0]}]", end=' ')
print()





