#Desenvolva um programa que leia o comprimento de três retas e diga ao usúario se elas podem u não formar um triângulo.

# Regra =  Cada um dos outros dois tem que ser menor que o soma dos outros dois

print("-=-" * 20)
print("Análisador de Triâmgulos")
print("-=-"* 20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMA Triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR Triângulos")