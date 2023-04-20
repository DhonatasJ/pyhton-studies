x = float(input("Digite a primeira medida do triângulo: "));
y = float(input("Digite a segunda medida do triângulo: "));
z = float(input("Digite a terceira medida do triângulo: "));
xsum = x + y;
zsum = x + z;
ysum = y + z;

def isTriangulo(xsum, zsum, ysum):
    if xsum > z and ysum > x and zsum > y:
        return True;
    else:
        return False;

def isTriEquilatero(xsum, zsum, ysum):
    if xsum == zsum and zsum == ysum:
        return True
    else:
        return False

def isTriIsoceles(xsum, zsum, ysum):
    if xsum == zsum or zsum == ysum or xsum == ysum:
        return True
    else:
        return False

def isTriEscaleno(xsum, zsum, ysum):
    if xsum != zsum and zsum != ysum:
        return True
    else:
        return False

if isTriangulo(xsum, zsum, ysum) and isTriEquilatero(xsum, zsum, ysum):
    print("Seu triangulo é equilatero")
elif isTriangulo(xsum, zsum, ysum) and isTriIsoceles(xsum, zsum, ysum):
    print("Seu trinagulo é isoceles")
elif isTriangulo(xsum, zsum, ysum) and isTriEscaleno(xsum, zsum, ysum):
    print("Seu triangulo é escaleno")
else:
    print("Suas medidas não formam um triângulo");