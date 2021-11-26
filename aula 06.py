lista = [
    ["produto_1", 20],
    ["produto_2", 10],
    ["produto_3", 16],
    ["produto_4", 14],
    ["produto_5", 6],
    ["produto_7", 69]
]

# parte 1
def func(item): # cria funcao para retornar o indice 1
    return item[1]


lista.sort(key=func) #pede para ordenar a lista pela chave da funcao, que vai ordenar pelo indice 1 da lista
#lista.sort(key=func, reverse=True) vai fazer o reverso de cima, fazendo mostrar do mais caro pro mais barato

for i in lista:
    print(i)

#parte 2
#Faz a mesma coisa que acima, sem usar o "def func()"
lista.sort(key=lambda item: item[1])

for i in lista:
    print(i)