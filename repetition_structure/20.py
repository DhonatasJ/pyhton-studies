while True:
    n = int(input("Insert a number: "));
    if n > 16:
        print("Please, insert a number less than 16")
        continue
    else:
        n += 1
        break

fatorial = 1
for i in range(1,n):
    fatorial *= i
    i -= 1
print(fatorial);
