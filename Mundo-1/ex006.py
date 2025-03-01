# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
# obs: prestar atenção a ordem de prescedencia > (r = n **(1/2))
# exemplo 01
n= int(input("Digite um número: "))
d = n * 2
t = n * 3
r = n **(1/2)
print("O dobro de {} vale {}.".format(n,d))
print("O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.".format(n, t, n,r))

