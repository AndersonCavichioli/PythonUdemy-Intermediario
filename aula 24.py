"""
try - except
"""


def converte_valor(valor):
    try:
        valor = int(valor) #verifica se o numero pode ser convertido pra inteiro
        return valor
    except ValueError:
        try:
            valor = float(valor) #verifica s eo numero pode ser convertido pra float
            return valor
        except ValueError:
            pass #se nao puder nenhum dos 2 acima, retorna none


n = converte_valor(input("Digite um numero: "))

if n is not None:
    print(n * 5)

else:
    print("Isso nao é numero")