vetor = []
sumVetor = 0
multVetor = 1
for i in range(5):
    nums = int(input(f"Enter the {i+1}º integer number: "))
    vetor.append(nums)
for i in vetor:
    sumVetor += i
    multVetor *= i 

print(f"The sum of values is {sumVetor}")
print(f"The multiplication of values is {multVetor}")
print(f"List of values {vetor}")

