"""
3 - crie uma funcao que receba 2 numeros. o primeiro é um valor e o segundo um percentual (ex. 10%). retorne (retur)
o valor do primeiro numero somado com o aumento do percentual do mesmo.
"""


def aumento():
    valor = float(input("Digite o salario: "))
    p1 = float(input("Digite a porcentagem de aumento: "))
    p2 = (p1 / 100) * 100

    total = valor + (valor * p1)

    if p1 > 100:
        return f"Porcentagem de aumento superior a 100%"

    else:
        return f"Valor: {valor} \nPorcentagem de aumento: {p2:.0f}% \nTotal com aumento: {total}"


print(aumento())
