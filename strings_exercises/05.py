name = input("Insert your name: ")

def change(name):
    x = []
    for i in name:
        x.append(i)
        x.pop()
        z = "".join(x)
        print(z)
    return name
print(change(name))