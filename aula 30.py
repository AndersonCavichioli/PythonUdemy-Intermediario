"""
mutavel - listas, dicionarios
"""


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []

    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ["Fabricio"]
clientes1 = lista_de_clientes(["Anderson", "Joao", "Jessica"])
clientes2 = lista_de_clientes(["Marcia", "Ana", "Arthur", "Ricardo"])
clientes3 = lista_de_clientes(["Andressa", "Larissa", "Ana", "Roberto"])

print(clientes1)
print(clientes2)
print(clientes3)

