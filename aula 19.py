"""
combinations, permutations e product - itertools
combinacao - ordem nao importa
permutacao - ordem importa
ambos nao repetem valores unicos
produto - ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product, count

lista = ["Anderson", "Carlos", "Beatriz", "Carol", "Joao"]

for grupo in combinations(lista, 2):
    print(grupo)

print("*" * 50)

for grupo in permutations(lista, 3):
    print(grupo)

l = []
i = 1

for i in range(61):
    l.append(i)

for mega in combinations(l, 6):
    print(mega)


