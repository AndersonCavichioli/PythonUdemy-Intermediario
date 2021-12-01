"""
count - itertools
"""

from itertools import count

contador = count() #cria o contador

for valor in contador:
    print(valor)

    if valor >= 10:
        break

contador = count(start=5, step=2) #inicia o contador em 5, pulando de 2 em 2

for valor in contador:
    print(valor)

    if valor >= 10:
        break

contador = count()
lista = ["Anderson", "Carlos", "Eduardo", "Julia", "Erica"]

lista = zip(contador, lista)

print(list(lista))