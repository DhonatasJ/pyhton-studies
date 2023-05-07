listNums = []
numsSquare = []
for i in range(10):
    num = int(input(f"Insert the {i+1}° integer number: "))
    listNums.append(num)
for i in listNums:
    x = pow(i,2)
    numsSquare.append(x)

print(f"Square values is {numsSquare}")