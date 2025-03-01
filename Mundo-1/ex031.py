#Desenvolva um programa que pergunta a distância de uma viagem em km.
#Calcule o preço da passagem,cobrando R$0.50 por km para viagens de até 200KM.
#E R$0.45 para viagens mais longas.


#Exercicio de condicional composta

#exemplo 1
"""distância = float(input("Qual é a distância da sua viagem?"))
print("Você está prestes a começar uma viagem de {}Km.".format(distância))
if distância  <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print("E o preço da sua passagem será de {:.2f}".format(preço))"""


#exemplo 2
distância = float(input("Qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km,".format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print("E o preço da sua passagem será de {:.2f}.".format(preço))
