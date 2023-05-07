data = []
dataList = []
heights = []
alt = [] 
agesPlus13 = []
heightsPlus13 = []
count = []
for j in range(30):
    for i in range(1):
        age = int(input(f"Insert the age of the {j+1}° person " ))
        height = float(input(f"Insert the height of the {j+1}° person " ))
    data = [age, height]
    dataList.append(data)

for i in dataList:
    a = i[1]
    heights.append(a)
mediaHeights = sum(heights) / len(heights)

for i in dataList:
    if i[0] > 13:
        agesPlus13.append(i)

for i,j in enumerate (agesPlus13):
    heightsPlus13.append(j[1])

for i in heightsPlus13:
    if i < mediaHeights:
        count.append(i)

print(f"{len(count)} alunos maiores que 13 anos e abaixo da media do peso da media de todos os alunos.")