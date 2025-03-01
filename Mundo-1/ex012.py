#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% desconto.
#formula para % = R$100*5/100 =5%
# 10,00 correspode a  100%
# X correspode a 5%
# multiplica-se de forma cruzada 10 por 5 e 100 por X = 10*5/100 = 0,5

preço = float(input("Qual é o preço do produto? R$"))
novo = preço - (preço * 5 / 100)
print ("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.".format(preço,novo))
