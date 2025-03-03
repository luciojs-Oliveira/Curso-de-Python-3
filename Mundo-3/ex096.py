
"""
Exercício Python 096:
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def área(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg:.0f} x {comp:.0f} é de {a:.0f},m².")


print('  Controle de Terrenos  ')
print(' = ' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento: '))
área(largura, comprimento)



