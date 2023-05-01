par = []
impar = []
for i in range(1, 11):
    x = int(input(f"Insert the {i}° number: "));
    if x % 2 == 0:
        par += [x]
    if x % 2 != 0:
        impar += [x]
print(par)
print(impar)
