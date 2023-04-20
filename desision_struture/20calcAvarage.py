n1 = float(input("First note: "));
n2 = float(input("Second note: "));
n3 = float(input("Third note: "));

media = (n1 + n2 + n3) / 3;

if media == 10:
    print("Aprovado com distinção!")
elif media >= 7 and media < 10:
    print("Aprovado!")
elif media < 7:
    print("Reprovado!")