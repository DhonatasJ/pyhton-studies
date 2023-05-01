n = int(input("Insira quantas vezes deseja calcular a media: "))
notas = []
for i in range(n):
    nota = float(input(f"Insira o {i+1}⁰ numero "))
    notas.append(nota)
nsum = sum(notas)
media = nsum / n
print(f"A media é {round(media, 2)}")