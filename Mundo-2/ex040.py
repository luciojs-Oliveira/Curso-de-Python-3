
'''
Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
'''

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("Tirando {:.1f} e {:.2f}, a média do aluno é {:.1f}".format(n1, n2, m))
if m >= 5 and m < 7:
    print("O aluno está em RECUPERAÇÃO !")
elif m < 5:
    print("O aluno está REPROVADO !")
elif m >= 7:
    print("O aluno está APROVADO!")






