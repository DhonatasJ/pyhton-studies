saltos = []

nm = input("Atleta: ")
for i in range(1):
    s1 = float(input("Primeiro Salto: " ))
    s2 = float(input("Segundo Salto: "  ))
    s3 = float(input("Terceiro Salto: " ))
    s4 = float(input("Quarto Salto: " ))
    s5 = float(input("Quinto Salto: " ))
    saltos.extend([s1, s2, s3, s4, s5])

print(f"Atleta: {nm}")
print("Saltos:", ", ".join([f"{s:.2f} m" for s in saltos]))
print(f"Media {sum(saltos) / len(saltos)})")