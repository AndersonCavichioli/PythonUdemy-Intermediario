"""
list comprehension
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [a for a in l1] #faz a iteração de cada valor contido na lista
print(ex1)

ex2 = [a * 2 for a in l1] #multiplica por 2 cada iteracao que passar na lista
print(ex2)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ["luiz", "mauro", "maria"]
ex4 = [v.replace('a', '@').upper() for v in l2] #substitui a por @ e joga tudo pra maiusculo
print(ex4)

tupla = (
    ("chave", "valor"),
    ("chave_2", "valor_2")
)
print(tupla)
ex5 = [(y, x) for x, y in tupla] #inverte chave e valor
print(ex5)

l3 = list(range(21)) #cria lista com 21 posicoes, indo do 0 ao 20
print(l3)
ex6 = [v for v in l3 if v % 2 == 0 if v % 3 == 0] #pega todos os numeros da lista que seja divisivel por 2 e por 3
print(ex6)

