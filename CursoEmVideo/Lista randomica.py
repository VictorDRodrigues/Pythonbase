import random

tamanho_lista = 5
inicio_intervalo = 1
fim_intervalo = 10

lista_randomica = random.sample(range(inicio_intervalo, fim_intervalo + 1), tamanho_lista)
print(lista_randomica)

lista_randomica.sort()

print(lista_randomica)