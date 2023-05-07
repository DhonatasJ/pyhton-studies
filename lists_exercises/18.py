votos = []
votosInd = []
while True:
    voto = int(input("Insert a number between 1 and 23: "))
    if not voto < 0 and voto > 23:
        print("Player invalid...")
        voto = int(input("Insert a number between 1 and 23: "))
    elif voto == 0:
        print("VOTATION CLOSED")
        break
    else:
        votos.append(voto)

print(f"Total computed votes {len(votos)}")

for i in votos:
    if i == i:
        votosInd.append(i)
print(votosInd)