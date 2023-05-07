votos = []
while True:
    voto = int(input("Insert a number between 1 and 23: "))
    if not voto < 0 and voto > 23:
        print("Player invalid...")
        voto = int(input("Insert a number between 1 and 23: "))
    elif voto == 0:
        print("VOTATION CLOSED")
        break
    elif voto > 0 and voto <= 23:
        votos.append(voto)
votosLen = len(votos)
print(f"Total computed votes {len(votos)}")
print(f"All votes: {votos}")
votos = [3, 2, 5, 23, 11, 12, 6, 2, 4, 6, 2, 4, 6, 6, 3, 4, 2, 4]
total_votes = len(votos)

vote_counts = {}
for vote in votos:
    if vote in vote_counts:
        vote_counts[vote] += 1
    else:
        vote_counts[vote] = 1

for candidate, count in vote_counts.items():
    percentage = (count / total_votes) * 100
    print(f"Candidato {candidate}: {percentage:.2f}%")
