"""
funcao filter()
"""
from dados import produtos, pessoas, lista


l1 = list(filter(lambda x: x > 5, lista))
print(l1)

l2 = list(filter(lambda p: p["preco"] > 10 and p["preco"] < 30, produtos)) #mostra somente os precos acima de 10 e abaixo de 30
for x in l2:
    print(x)


def filtra(produto):

    if produto["preco"] > 10 and produto["preco"] < 30: #faz o mesmo que os comandos acima, porem, usando uma funcao
        return True


l3 = list(filter(filtra, produtos))

for produto in l3:
    print(produto)

print()

def maior(pessoa): #faz um filtro apenas em idades maior ou igual a 18

    if pessoa["idade"] >= 18:
        return True
        #pessoa["é de maior"] = True
        #return True
    else:
        return False


l4 = filter(maior, pessoas)

for idades in l4:
    print(idades)
