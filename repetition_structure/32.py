n = int(input("Insert a number: "));
n += 1
fatorial = 1
for i in range(1,n):
    fatorial *= i

list = []
for i in range(1,n):
    list.append(i)
list.reverse()

x = str(type(list))
print(x)