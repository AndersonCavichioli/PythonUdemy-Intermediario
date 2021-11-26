"""
Tuplas - Tuplas são quase iguais a listas, porém, os valores dela nao podem ser alterados, as tuplas sao imutaveis!!
obs.: caso precise alterar o valor dela, converta-a para lista, altere ou acrescente e transforme-a em tupla novamente
"""

tupla = 1, 2, 3, 4, 5
print(type(tupla))
print(tupla)

tupla = list(tupla) # converte para lista
print(tupla)

tupla[1] = "anderson" # altera o indice 1 para anderson
print(tupla)

tupla = tuple(tupla) # converte novamente para tupla
print(tupla)