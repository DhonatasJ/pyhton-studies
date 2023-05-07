n = int(input("Input a number: "))

def printNums(n):
    for i in range(1, n+1):
        for j in range(i):
            print(j+1, end=" ")
        print()
printNums(n)