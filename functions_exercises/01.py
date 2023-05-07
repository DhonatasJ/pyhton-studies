n = int(input("Insert a integer number: "))

def printNum(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()
printNum(n)