'''
Exercício Python 73:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
         "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", "Curitiba",
         "Avaí", "Ponte Preta")
print("\033[35m-=\033[m" * 100)
print(f"Lista de times do Brasileirão:{times}")  # Mostrar a lista de times usa se fstring + mascara{}
print("\033[35m-=\033[m" * 100)
print(f"Os 5 Primeiros são{times[0:5]}")  # Usa - se Fatiamento
print("\033[34m-=\033[m" * 100)
print(f"Os 4 últimos são  {times[-4:]}")  # Usa - se Fatiamento
print("\033[34m-=\033[m" * 100)
print(f"Times em ordem alfabetica: {sorted(times)}")  # Usa - se sored para Ordenamento
print("\033[33m-=\033[m" * 100)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ªposição')  # Usa - se .index  para localizar uma determinda posição.
print("\033[33m-=\033[m" * 100)
