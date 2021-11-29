"""
dict comprehension
"""

lista = [
    ("chave_1", "valor_1"),
    ("chave_2", "valor_2"),
]

d1 = {x : y for x, y in lista}
print(d1)

