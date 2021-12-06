"""
criando, lendo, escrevendo e apagando arquivos
"""
#parte 1
file = open("arquivo.txt", "w+") #w+ significa leitura e escrita
file.write("Linha 1 \n")
file.write("Linha 2 \n")
file.write("Linha 3 \n")

file.seek(0, 0) #vai setar o cursor pra posicao 0 e ler o arquivo
print(file.read())

file.seek(0, 0) #volta o cursor pra posicao 0 do arquivo
print(file.readline(), end='') #le a linha 1, o end serve pra nao dar quebra de linha
print(file.readline(), end='') #vai pra linha 2
print(file.readline(), end='') #vai pra linha 3

print() #quebra de linha pra visualização

#parte 2
file.seek(0, 0)
print(file.readlines()) #utilizando lines no plural joga tudo pra dentro de uma lista

print() #quebra de linha

#parte 3
file.seek(0, 0)
for x in file.readlines(): #le cada linha da lista que foi criada com o readlines
    print(x, end='')

file.close()

print() #quebra de linha

#parte 4
with open("arquivo2.txt", "w+") as file2: #utilizando o with ofen nao ha necessidade de usar o .close(), sendo essa a maneira mais pytonica de se trabalhar
    file2.write("Linha 1 \n")
    file2.write("Linha 2 \n")
    file2.write("Linha 3 \n")

    file2.seek(0)
    print(file2.read())

print() #quebra de linha

#parte 5
with open("arquivo2.txt", "r") as file3: #r é somente para leitura
    print(file3.read())

with open("arquivo.txt", "a+") as file4: #a+ significa modo append, vai escrever mais coisas no arquivo, sem apagar o restante. se usar w+ ele sobrescreve o arquivo
    file4.write("linha 4 \n") #adiciona linha 4 no arquivo
    file4.write("linha 5 \n") #adiciona linha 5 no arquivo

    file4.seek(0)
    print(file4.read())

#parte 6
import os

os.remove("nome_do_arquivo.txt") #remove o arquivo do diretorio
