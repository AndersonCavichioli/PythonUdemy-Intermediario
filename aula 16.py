"""
zip - unindo iteraveis
zip_longest - unindo itertools
"""
from itertools import zip_longest

#codigo
cidades = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo"]

#codigo
estados = ["SP", "MG", "BA"]

"""cidades_estados = zip(cidades, estados)"""
"""print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))"""


"""for valor in cidades_estados: #faz o mesmo que o codigo acima, porem usando o for
    print(valor[0], valor[1])"""

"""for valor in cidades_estados: #faz o mesmo que o codigo acima porem joga pra dentro de tuplas
    print(valor)"""

cidades_estados = zip_longest(estados, cidades, fillvalue="estado") # fillvalue cria um nome pra usar nos nones
"""print(list(cidades_estados))"""

for a in cidades_estados:
    print(a)