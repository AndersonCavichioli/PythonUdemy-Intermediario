carrinho = []

carrinho.append(("produto 1", 30)),
carrinho.append(("produto 2", 110)),
carrinho.append(("produto 3", 97)),
carrinho.append(("produto 4", 60)),

total = 0
for produto in carrinho:
    total += produto[1]
print(total)

total2 = sum([float(y) for x, y in carrinho])
print(total2)