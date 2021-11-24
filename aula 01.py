"""
Funçoes - def em python
"""


def saudacao(msg="ola", nome="usuario"):
    print(msg, nome)


saudacao("Hellooo", "Anderson")  # recebe msg e nome definido aqui
saudacao(nome="Andre")  # Define um nome a variavel nome
saudacao()  # recebe os valores padroes definidos na funcao def


def saudar(msg="ola", nome="Usuario"):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{nome} {msg}'


variavel = saudar()
print(variavel)


def somar(a=input("Digite n1:"), b=input("Digite n2: ")):
    a = int(a)
    b = int(b)
    soma = a + b
    return f"{soma}"


s = somar()
print(s)
