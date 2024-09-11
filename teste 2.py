#produtos
pp = "pizza pequena"
pm = "pizza média"
pg = "pizza grande"

#preços
p = 30.00
m = 50.00
g = 70.00

produtos = input(f"{pp} R$ {p}\n{pm} R$ {m}\n{pg} R$ {g}\nEscolha o tamanho das pizzas:")

if (produtos == pp):
    print("A pizza escolhida foi a pequena.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = p * quantidade
    print("------------------------------------")
    print(f"Você comprou {quantidade} x {pp}/s")
    print(f"Sua compra total foi: R${total}")

elif (produtos == pm):
    print("A pizza escolhida foi a média")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = m * quantidade
    print("------------------------------------")
    print(f"Você comprou {quantidade} x {pm}/s")
    print(f"Sua compra total foi: R${total}")

elif (produtos == pg):
    print("A pizza escolhida foi a grande")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = g * quantidade
    print("------------------------------------")
    print(f"Você comprou {quantidade} x {pg}/s")
    print(f"Sua compra total foi: R${total}")

else:
    print("Tipo de pizza invalido")
