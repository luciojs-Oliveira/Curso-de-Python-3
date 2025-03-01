#Faça um programa qua leia a largura e a altura de uma parede em metros,calcule a sua área e a quantidade de tinta necessária para pinta-lá,
# sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input("A largura da parede:"))
alt =  float(input("Altura da parede: "))
área = larg * alt
print("A Sua parede tem a dimensão de {} x {} e sua área é de {}m²".format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede, você precisará de {} Litros de tinta ".format(tinta))