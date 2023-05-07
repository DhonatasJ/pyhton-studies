allNotas = []
inMedia = []
for i in range(10):
    notas = []
    for j in range(4):
        n = float(input(f'Insira a nota {j+1}ª nota do {i+1}º aluno: '))
        notas.append(n)
    allNotas.append(notas)
for x in allNotas:
    if (sum(x) / len(x)) >= 7:
        media = sum(x) / len(x)
        print(f"As médias maiores que 7 são {media:.2f}")