x = int(input("Insert a number: "))

def reverse(x):
    xStr = str(x)
    rev = xStr[::-1]
    return rev

print(reverse(x))