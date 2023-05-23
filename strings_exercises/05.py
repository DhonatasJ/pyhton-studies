name = input("Insert your name: ")

def change(name):
    x = []
    for i in name:
        x.append(i)
    for i in enumerate (name):
        print("".join(x))
        x.pop()
    return x
print(change(name))