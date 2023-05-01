cityA = float(input("Insira a população da cidade menor: "));
a = cityA;
cityB = float(input("Insira o população da cidade maior: "));
b = cityB;
p1 = float(input("Insira a porcentagem de crescimento da primeira cidade: "));
p2 = float(input("Insira a porcentagem de crescimento da segunda cidade: "));
porcentA = (cityA / 100) * p1;
porcentB = (cityB / 100) * p2;
y = 0;

while a <= b:
    a *= cityA + porcentA
    b *= cityB + porcentB
    y += 1
    if a >= b:
        print(f"{y} Years")
        break;