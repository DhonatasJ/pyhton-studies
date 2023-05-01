x = int(input("Insira o numero da base: "));
y = int(input("Insira o expoente: "));

result = 1;
for i in range(y):
    result *= x;
print(result)
