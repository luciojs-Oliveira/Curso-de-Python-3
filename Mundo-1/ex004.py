#Faça um programa que leia pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveís sobre ela.
a = input("Digite algo: ")
print("O tipo desse valor é:", type(a))
print("Só tem espeçõs? ", a.isspace())
print("É alfabético?", a.isnumeric())
print("É alfanumerico?", a.isalnum())
print("Está em maiscula?",a.isupper())
print("Está em minuscula ", a.islower())
print("Está capitalizada?", a.istitle())
