vlrpao = float(input("Insira o preço da unidade de pão "))
tabela = []
for i in range(1, 51):
    tabela = vlrpao * i
    print(f"{i} pães custa R${tabela:.2f}")

