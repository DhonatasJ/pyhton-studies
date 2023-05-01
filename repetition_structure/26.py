eleitores = int(input('Insira a quantidade de eleitores '))
votos = []
for i in range(eleitores):
    for i in range(1):
        print("Vota 'X' para o 1⁰ candidato 'Z' para o 2⁰ e 'Y' para o 3⁰")
        voto = input(f"Vote no seu candidato ")
        votos.append(voto)

x = list(filter(lambda x:x == "x", votos))
z = list(filter(lambda x:x == "z", votos))
y = list(filter(lambda x:x == "y", votos))
print(f"O primeiro candito tem {len(x)} votos")
print(f"O segundo candito tem {len(z)} votos")
print(f"O terceito candito tem {len(y)} votos")
