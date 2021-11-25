"""
4 - Fizz Buzz - Se o parametro da fguncao for divisivel por 2, retorne fizz,
se o parametro da funcao for divisivel por 5, retorne buzz, se o paramentro
da funcao for divisivel por 5 e por 3 retorne FizzBuzz, caso contrario, retorne o numero inviado
"""


def fizzbuzz():
    n = int(input("Digite um numero: "))
    if n % 3 == 0 and n % 5 == 0:
        return f"FizzBuzz"

    elif n % 5 == 0:
        return f"Buzz"

    elif n % 3 == 0:
        return f"Fizz"

    else:
        return f"{n}"



print(fizzbuzz())

