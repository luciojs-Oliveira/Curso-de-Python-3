galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print(f'As mulhers cadastradas forams.', end=" ")
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=" ")
print()
print(f'lista das pessoas que estão acime da média:')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}:', end=' ')
print('<< ENCERRADO >>')




