peso = []
altura = []
menorPeso = float('inf')
menorAltura = float('inf')
maiorPeso = 0
maiorAltura = 0

cod = int(input("Insira o código do cliente ou '0' para finalizar. "))
while cod != 0:
        pesoX = float(input("Insira o peso do cliente: "))
        alturaY = float(input("Insira a altura do cliente: "))
        peso.append(pesoX)
        altura.append(alturaY)

        if pesoX < menorPeso:
            menorPeso = pesoX
            codMenorPeso = cod

        if alturaY < menorAltura:
            menorAltura = alturaY
            codMenorAltura = cod

        if pesoX > maiorPeso:
            maiorPeso = pesoX
            codMaiorPeso = cod

        if alturaY > maiorAltura:
            maiorAltura = alturaY
            codMaiorAltura = cod

        cod = int(input("Insira o código do cliente ou '0' para finalizar. "))

print(f"Menor peso é do cliente {codMenorPeso} que é {menorPeso} ")
print(f"Menor altura é do cliente {codMenorAltura} que é {menorAltura}")
print(f"Maior peso é do cliente {codMaiorPeso} que é {maiorPeso}")
print(f"Maior altura é do cliente {codMaiorAltura} que é {maiorAltura}")
print(f"A media de peso {sum(peso) / len(peso):.2f}")
print(f"A media de altura {sum(altura) / len(peso):.2f}")

