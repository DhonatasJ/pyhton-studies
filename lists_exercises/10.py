fVector = []
sVector = []
vectorFull = []

for i in range(5):
    vector1 = int(input(f"Insert the {i+1}° integer of first vector: "))
    fVector.append(vector1)
for i in range(5):
    vector2 = int(input(f"Insert the {i+1}° integer of second vector: "))
    sVector.append(vector2)

maxLoop = max(len(fVector), len(fVector))

for i in range(maxLoop):
    if i < len(fVector):
        vectorFull.append(fVector[i])
    if i < len(sVector):
        vectorFull.append(sVector[i])
print(f"Interleaved list {vectorFull}")