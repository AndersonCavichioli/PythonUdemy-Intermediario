"""
2 - crie uma funcao que recebe 3 numeros como paramertos e exiba a soma entre eles
"""

def soma():
    n1 = int(input("Digite n1: "))
    n2 = int(input("Digite n2: "))
    n3 = int(input("Digite n3: "))

    s = n1 + n2 + n3

    return f"a soma de {n1}+{n2}+{n3} é = {s}"

print(soma())