name = input("Insert your name: ")

def change(name):
    x = []
    for i in name:
        x.append(i)
        z = "".join(x)
        print(z)
    return z
print(change(name))