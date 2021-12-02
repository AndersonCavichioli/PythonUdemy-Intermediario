"""
funcao filter()
"""
from dados import produtos, pessoas, lista


l1 = list(filter(lambda x: x > 5, lista))
print(l1)

l2 = list(filter(lambda p: p["preco"] > 10 and p["preco"] < 30, produtos)) #mostra somente os precos acima de 10 e abaixo de 30
for x in l2:
    print(x)



