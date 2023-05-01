n = int(input("Insert a number: "))
a,b = 0,1

for i in range(n):
    a, b = b, a + b
    if b <= 500:
        print(b,end=" ");
