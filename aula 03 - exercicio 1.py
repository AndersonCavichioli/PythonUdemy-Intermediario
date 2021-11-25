"""
1 - crie uma função que exibe uma saudação com os parametros saudação e nome.
"""


def saudacao():
    s = "Olá"
    n = "Usuário"

    nome = input("Qual o seu nome? ")
    if nome == "":
        return f"{s}, {n}"
    else:
        return f"{s}, {nome}"


print(saudacao())
