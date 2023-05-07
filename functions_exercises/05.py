def somaImposto(taxaImposto,custo):
    custoPor = (custo * taxaImposto) / 100
    liquid = custo - custoPor
    return liquid
taxaImposto = float(input("Insira a taxa de imposto sob o produto que informará o produto abaixo: "))
custo = float(input("Insira o custo do produto do produto: " ))
result = somaImposto(taxaImposto,custo)
print(f"R$ {result:.2f}")