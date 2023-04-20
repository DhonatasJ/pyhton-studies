valor = int(input("Qual o valor do saque? (mínimo R$10 e máximo R$600): "))

if valor < 10 or valor > 600:
    print("Valor inválido. Tente novamente.")
else:
    notas_100 = valor // 100
    valor = valor % 100

    notas_50 = valor // 50
    valor = valor % 50

    notas_10 = valor // 10
    valor = valor % 10

    notas_5 = valor // 5
    valor = valor % 5

    notas_1 = valor

    print(f"Notas de R$100: {notas_100}")
    print(f"Notas de R$50: {notas_50}")
    print(f"Notas de R$10: {notas_10}")
    print(f"Notas de R$5: {notas_5}")
    print(f"Notas de R$1: {notas_1}")
