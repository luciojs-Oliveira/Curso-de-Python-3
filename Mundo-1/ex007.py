#Desenvolva um programaque leia as duas notas de um aluno, calcule  e mostre a sua média.
# obs: prestar atenção a ordem de prescedencia > (nota1 + nota2) / 2  1°adição depois a divisão
# Para aredondar um numero fracionado usa se {:.1f} = (Depois do ponto flutuante coloque apenas um digito) que fará o aredondamento do numero para cima.
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
média = (nota1 + nota2) / 2
print("A media entre {:.1f} e {:.1f} é igual a {:.1f}:".format(nota1,nota2,média))


