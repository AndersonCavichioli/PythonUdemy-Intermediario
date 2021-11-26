"""
Dicionarios
"""
#opção 1
d1 = {"chave_1": "valor da chave 1"} #cria o dicionario d1
d1["chave_2"] = "valor da chave 2" #inclui chave 2 no dicionario d1

print(d1)

#opção 2
d2 = dict(chave_1="valor da chave 1", chave_2="valor da chave 2")
print(d2["chave_1"])
print(d2)

"""#Exercicio teste meu - teste input com laço de repetição

qtde = int(input("Quantos cadastros deseja adicionar: ")) #pede o tamanho do dicionario
dicionario = {}

for i in range(qtde): # para i em quantidade digitada
    a = input("Digite o nome: ") # variavel a recebe o input
    if i <= qtde: #caso i seja menor que a quantidade digitada
        dicionario[i] = a #dicionario recebe o input
    i+= 1

print(dicionario)"""

#opção 3

d1 = {
    "str": "uma string",
    123: "valores inteiros",
    (1,2,3,4): "Tupla"
}

if d1.get("str") is not None:
    print("Essa chave existe")
else:
    print(123)

#opção 4

dic2 = {
    "nome_1": "anderson",
    "nome_2": "ricardo",
    "nome_3": "angela"
}

print(dic2.get("nome_1"))

#opção 5 - update

dic2.update({"nome_4": "carolina"})
print(dic2)

#opção 6 - consultar o 2 valor de dentro do dicionario

dic2 = {
    "nome_1": "anderson",
    "nome_2": "ricardo",
    "nome_3": "angela"
}

print('anderson' in dic2.values())

#opção 7 - conta quantos pares existem no dicionario

print(len(dic2))

#opção 8 - iterar sobre o dicionario

for i in dic2:
    print(i) # mostra a posicao 1 do dicionario

for k in dic2.values():
    print(k) # mostra a posicao 2 do dicionario

for a in dic2.items():
    print(a) #mostra o conteudo do dicionario

for b in dic2.items():
    print(b[0], b[1]) #tira de dentro da lista

for b, c in dic2.items():
    print(b, c) #faz o mesmo que o de cima mas desempacotando

for b, c in enumerate(dic2.items()):
    print(b, c) #faz o mesmo que o de cima enumerando cada um com um indice

#opção 9

dic3 = {
    1: "anderson",
    2: "carlos",
    3: "joao",
    4: "maria"
}

print(dic3)
dic3.pop(1) #apaga o 1
print(dic3)
dic3.popitem() #apaga o ultimo elemento da lista
print(dic3)
dic3.update({4: "natalia"}) #acrescente a posicao e o nome dentro do dicionario
print(dic3)
