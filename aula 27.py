from vendas.calc_preco import aumento, reducao

preco = float(input("Digite o preço pra aumentar: "))
p = int(input("Digite a porcentagem inteiro: "))

aumentar = aumento(valor=preco, porcentagem=p)
print(aumentar)

preco_2 = float(input("Digite o preco pra reduzir: "))
p2 = int(input("Digite a porcentagem inteiro: "))

reduzir = reducao(valor=preco_2, porcentagem=p2)
print(reduzir)

