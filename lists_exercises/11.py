fVector = []
sVector = []
tVector = []
vectorFull = []

for i in range(10):
    vector1 = int(input(f"Insert the {i+1}° integer of first vector: "))
    fVector.append(vector1)
for i in range(10):
    vector2 = int(input(f"Insert the {i+1}° integer of second vector: "))
    sVector.append(vector2)
for i in range(10):
    vector3 = int(input(f"Insert the {i+1}° integer of third vector: "))
    tVector.append(vector3)

maxLoop = max(len(fVector), len(sVector), len(tVector))

for i in range(maxLoop):
    if i < len(fVector):
        vectorFull.append(fVector[i])
    if i < len(sVector):
        vectorFull.append(sVector[i])
    if i < len(tVector):
        vectorFull.append(tVector[i])
print(f"Interleaved list {vectorFull}")