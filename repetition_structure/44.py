print("Candidato", "Códigos do candidato ")
print("Jose          ", 1)
print("João          ", 2)
print("Mara          ", 3)
print("Gabi          ", 4)
print("Voto Nulo     ", 5)
print("Voto em Branco", 6)
votos = []

while True:
    cand = int(input("Insira o codigo do candidato, voto nulo ou em branco: "))
    votos.append(cand)
    if cand == 0:
        print("Encerrando votação...")
        break

jose = list(filter(lambda x: x in [1], votos))
joao = list(filter(lambda x: x in [2], votos))
mara = list(filter(lambda x: x in [3], votos))
gabi = list(filter(lambda x: x in [4], votos))
voto_nulo = list(filter(lambda x: x in [5], votos))
voto_em_branco = list(filter(lambda x: x in [6], votos))

vn = len(voto_nulo)
tmn = len(votos)
sumVotos = tmn-1
porcent1 = (vn * 100) - (sumVotos * 100)


print(f"Jose obteve {len(jose)} votos")
print(f"João obteve {len(joao)} votos")
print(f"Mara obteve {len(mara)} votos")
print(f"Gabi obteve {len(gabi)} votos")
print(f"{len(voto_nulo)} votos Nulo")
print(f"{len(voto_em_branco)} votos em Branco")
print(f"A percentagem de votos nulos sobre o total de votos é {porcent1:.2f}%")