tabuadaDe = int(input("Insira o valor que deseja a tabuada: "))
comeco = int(input("Insira o valor que deseja a comecar a tabuada: "))
fim = int(input("Insira o valor que deseja a terminar a tabuada: "))

for i in range(comeco, fim+1):
    x = tabuadaDe * i
    print(f"{tabuadaDe} x {i} = {x}")