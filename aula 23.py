"""
Reduce
"""

from dados import produtos,pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i : i + ac, lista) #faz a soma de todos os itens da lista "lista"
print(soma_lista)

print()

soma_produtos = reduce(lambda ac, p : p["preco"] + ac, produtos, 0) #faz a soma de todos os precos da lista "produtos"
print(soma_produtos)

print()

media = reduce(lambda ac, p : p["preco"] + ac, produtos, 0) #faz a media de valores de todos os precos da lista "produtos"
m = media / len(produtos)
print(m)

soma_idades = reduce(lambda ac, i : i["idade"] + ac, pessoas, 0) #faz a soma das idades contidas na lista pessoas
print(soma_idades)

media_idades = reduce(lambda ac, p : p["idade"] + ac, pessoas, 0) #faz a media das idades contidas na lista pessoas
md = media_idades / len(pessoas)
print(md)


