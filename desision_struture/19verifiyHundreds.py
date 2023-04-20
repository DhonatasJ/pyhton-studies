num = input("Insira um numero: ");
numLen = num.zfill(3);
unid = numLen[-1];
deze = numLen[-2];
cent = numLen[-3];


if unid == "0":
    print("")
elif unid == "1":
    print(unid + " unidade ")
else:
    print(unid + " unidades ")

if deze == "0":
    print("")
elif deze == "1":
    print(deze + " dezena ")
else:
    print(deze + " dezenas ")

if cent == "0":
    print("")
elif cent == "1":
    print(cent + " centena ")
else:
    print(cent + " centenas ");


