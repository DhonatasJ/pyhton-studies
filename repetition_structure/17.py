n = int(input("Insert a number: "));
n += 1
fatorial = 1
for i in range(1,n):
    fatorial *= i
    i -= 1
print(fatorial);