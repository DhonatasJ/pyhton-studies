cds = int(input("Informa a quantidade de CDs da sua coleção "))
sumcds = 0
for i in range(cds):
    prices = float(input("Informe o valor do {i} CD "))
    sumcds += prices

print(f"Voce gastou R${sumcds:.2f} em sua colecao")
print(f"Em media o valor gasto para cada um foi R${sumcds/cds:.2f}")