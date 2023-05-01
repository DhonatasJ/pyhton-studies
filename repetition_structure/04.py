cityA = 80000;
a = 80000;
cityB = 200000;
b = 200000;
porcentA = (cityA / 100) * 3;
porcentB = (cityB / 100) * 1.5;
y = 0;

while a <= b:
    a *= cityA + porcentA
    b *= cityB + porcentB
    y += 1
    if a >= b:
        print(f"{y} Years")
        break;