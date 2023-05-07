notas = []
for i in range(5):
    x = float(input("Insira as notas "))
    notas.append(x)
print(f"As notas são {notas}")
print(f"A media das notas informadas é {sum(notas)/len(notas):.2f}")