#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input("Qual o salário do Funcionário? R$ "))
novo = salário + (salário * 15 / 100)
print("Um Funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário,novo))
