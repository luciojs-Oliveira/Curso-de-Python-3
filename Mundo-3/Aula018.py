'''
Aula - 18

'''

'''
teste = list() #Criar - lista()
teste.append('Gustavo') #Acrescentar - append
teste.append(40)
galera = list()
galera.append(teste[:])#Criar cópia de uma lista = [:] = colchetes + : cria nova lista
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

''''''
'''
galera =[['joão', 19], ['Ana', 33], ['joaquim', 13], ['maria', 45]]
for p in galera:
    print(p[0])
'''

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idde.')
        totmenor += 1

print(f'temos {totmaior} maiores e {totmenor} menores de idade.')










