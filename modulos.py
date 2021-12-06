"""
Módulos python
"""
import math

PI = math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


if __name__ == 'main': #Executa apenas se esse programa for executado, se for importado em outro arquivo, essa parte de baixo nao aparece

    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)