nums = []
numsPar = []
numsImpar = []
for i in range(20):
    num = int(input("Insert a integer number "))
    nums.append(num)

for i in nums:
    if i % 2 == 0:
        numsPar.append(i)
    else:
        numsImpar.append(i)
print(f"List numbers: {nums}")
print(f"List numbers PAR: {numsPar}")
print(f"List numbers IMPAR: {numsImpar}")