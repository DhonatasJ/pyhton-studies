temps = int(input("Insira a quantidade do conjunto de temperaturas que deseja informar: "))
listTemps = []
bigger = 0
for i in range(temps):
    x = float(input(f"Insira a {i+1}⁰ temperatura em graus: "))
    listTemps.append(x)
    if x > bigger:
        bigger = x
print(f"A media das temperaturas informadas é {sum(listTemps) / temps:.2f}⁰ graus")
print(f"A maior temperatura {bigger:.2f}⁰ graus")