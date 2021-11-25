"""
funcoes - args ***kwargs
"""


def func(*args):
    args = list(args)  # transforma a variavel args em uma lista
    args[0] = 20  # define a posição 0 da listra com valor 20
    print(args)


func(1, 2, 3, 4, 5)


def func2(*args):
    for v in args:
        print(v)


func2(1, 2, 3, 5, 7, 12, 36)


def func3(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
func3(*lista)  # Joga pra dentro de uma tupla -> ()
func(*lista, 10, 20, 30, 40, 50)


def func4(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs["nome", kwargs["Sobrenome"]])


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func4(*lista, *lista2, nome="Anderson", sobrenome="Cavichioli")
