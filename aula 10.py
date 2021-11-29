"""
sets - add (adiciona), update (atualiza) clear, discard
union | (une)
"""

s1 = set()
s1.add("anderson") #adiciona valor no set
s1.add("teste")
s1.add(1) #adiciona dentro do set
s1.add(2)
s1.add(3)
print(s1)

s1.discard(2) #deleta elementos do set
print(s1)

s2 = {1, 2, 3, 4}
s3 = {1, 3, 5, 6, 8, 9}

s4 = s2 | s3 # pipe | faz a uniao dos 2 sets
print(s4)

s5 = s2 - s3 #pega todos os elementos que tem no set 2 e nao tem no set 3
print(s5)

s6 = s2 ^ s3 #pega todos os elementos diferentes entre os 2 sets
print(s6)