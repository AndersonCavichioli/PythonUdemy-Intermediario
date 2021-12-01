#solucao 1
a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 3, 5, 6, 8, 7, 4, 6, 9, 2]

tam_a = len(a)
tam_b = len(b)

if tam_a > tam_b:
    soma = []

    for i in range(len(b)):
        soma.append(a[i] + b[i])

    print(soma)

elif tam_b > tam_a:
    soma = []

    for i in range(len(a)):
        soma.append(b[i] + a[i])

    print(soma)

    #solucao usando list comprehension
    soma2 = [x + y for x, y in zip(a, b)]
    print(soma2)