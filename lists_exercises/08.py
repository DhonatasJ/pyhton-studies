data = []
dt = []
position = 0
for i in range(5):
    for j in range(1):
        age = int(input(f"Insert the age of {i+1}º person: "))
        height = float(input(f"Insert the height of {i+1}º person:"))
    dt = [age, height]
    data.append(dt)

dataOrigin = data[:]
data.reverse()

for i, person in enumerate(data):
    age = person[0]
    height = person[1]
    print(f"The {i+1}° is {age} years old and {height} of height")