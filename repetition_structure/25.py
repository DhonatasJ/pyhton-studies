n = int(input("Insira a quantidade de pessoas que deseja inserir a idade: "))
idades = []
for i in range(n):
    idade = int(input(f"Insira a idade da {i+1}⁰ pessoa: "))
    idades.append(idade)
media = sum(idades) / n;

if media > 0 and media < 26:
    print("A turma é jovem.")
elif media > 25 and media <= 60:
    print("A turma é jovem.")
elif media > 60:
    print("A turma é idosa.")