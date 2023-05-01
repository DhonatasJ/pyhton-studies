x = int(input("Enter the smallest number: "))
y = int(input("Enter the larger number: "))
y += 1
num = []
for i in range(x, y):
    num += [i]
print(sum(num))
