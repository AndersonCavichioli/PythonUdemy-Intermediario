from dados import produtos, pessoas, lista

print(lista)

l1 = list(map(lambda x: x * 2, lista)) #multiplica cada componente da lista por 2
print(l1)

print()

l2 = [x *2 for x in lista] #mesma coisa do codigo acima usando list comprehensions
print(l2)

print()

for produto in produtos:
    print(produto)

print()
#pegar so os valores dos precos no dicionario

precos = map(lambda p: p['preco'], produtos)
for preco in precos:
    print(preco)

#aumentar 5% na coluna de precos

def aumento(p):
    p["preco"] = round(p["preco"] * 1.05, 2) #arredonda as casas decimais pra 2 com a funcao round
    return p


novos_produtos = map(aumento, produtos)

for produto in novos_produtos:
    print(produto)

print()
#pedgar somente o nome das pessoas no dicionario pessoas

nomes = map(lambda p: p["nome"], pessoas)

for pessoa in nomes:
    print(pessoa)

#aumentar a idade da lista de pessoas

def aumenta_idade(p):
    p["idade"] = p["idade"] + 4
    return p


nova_idade = map(aumenta_idade, pessoas)

#mostrar lista original
for y in pessoas:
    print(y)

print()

#mostrar lista com as idades alteradas
for x in nova_idade:
    print(x)

