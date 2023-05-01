print("Especificação", "Código", "Preço")
print('Cachorro Quente',100   , "R$ 1,20")
print('Bauru Simples  ',101   , "R$ 1.30")
print('Bauru com ovo  ',102   , "R$ 1.50")
print('Hamburguer     ',103   , "R$ 1.20")
print('Cheeseburguer  ',104   , "R$ 1.30")
print('Refrigerante   ',105   , "R$ 1.00")
soma = 0
while True:
    pedido = int(input("Insira o codigo do pedido, ou '0' para encerrar a compra: "))
    if pedido == 0:
        print("Pedido encerrado!") 
        break
    qtd = int(input("Insira a quantidade de lanches que deseja referente o pedido acima "))
    if pedido == 100:
        valor = qtd * 1.2
        soma += valor
        print(f"Custa R$ {valor:.2f}")
    elif pedido == 101:
        valor = qtd * 1.3
        soma += valor
        print(f"O valor a ser pago sera {valor:.2f}")
    elif pedido == 102:
        valor = qtd * 1.5
        soma += valor
        print(f"O valor a ser pago sera {valor:.2f}")
    elif pedido == 103:
        valor = qtd * 1.2
        soma += valor
        print(f"O valor a ser pago sera {valor:.2f}")
    elif pedido == 104:
        valor = qtd * 1.3
        soma += valor
        print(f"O valor a ser pago sera {valor:.2f}")
    elif pedido == 105:
        valor = qtd * 1
        soma += valor
        print(f"O valor a ser pago sera {valor:.2f}")

print(f"O valor total do seu pedido e R$ {soma:,.2f}")