name = input("Insert your name: ")

def change(name):
   x = name[::-1].upper()
   return x
print(change(name))