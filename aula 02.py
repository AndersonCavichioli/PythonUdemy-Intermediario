def divisao(n1, n2):
    if n2 > 0 and n1 > 0:
        return n1 / n2


divide = divisao(0, 2)

if divide:
    print(divide)
else:
    print("Conta invalida")

def multiplicacao():
    n1 = int(input("Digite N1: "))
    n2 = int(input("Digite N2: "))
    return n1 * n2

multi = multiplicacao()

print(f'o resultado é: {multi}')
