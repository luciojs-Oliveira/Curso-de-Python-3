'''
Exercício Python 076:
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

listagem = ("lápis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120,
            "Canetas", 22.30,
            "livro", 34.90)
print("\033[36m-" * 40)
print(f'{"Listagem De PREÇOS":^40}')
print("\033[36m-" * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'\033[35m{listagem[0]:.<30}', end=" ")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("\033[36m-" * 40)
