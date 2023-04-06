largura = float(input("Insert the width of wall: "));
altura = float(input("Insert the height of wall: "));
parede = largura * altura;
valorPLata = 80 / 18;
valorPGalao = 25 / 3.6;
ltCadaMetro = parede / 6;
lataInMetros = 18 * 6;
galaoInMetros = 3.6 * 6;
lata = 0;
qtdLata = 0;
galao = 0;
qtdGalao = 0;
liquidLata = 0;

while lata <= parede:
      lata += lataInMetros
      qtdLata += 1;
while galao <= parede:
    galao += galaoInMetros
    qtdGalao += 1;
valueLata = qtdLata * 80;
valueGalao = qtdGalao * 25;

lataEmLt = qtdLata * 108;
lataMenos = (lataEmLt / 100) * 10;
lataComBonus = parede + lataMenos;

if (qtdLata * 108) > lataEmLt:
    lataEnco = qtdLata - 1;

x = (qtdLata - 1) * 108
print(x)
print(lataComBonus)
galaoEnco = 0;
while x < parede:
    x += 21.6
    galaoEnco += 1;

print("Your wall measure is equal " + str(parede) + " meters.");
print("You will need buy " + str(qtdLata) + " tins, then will cost $ " + str(round(valueLata,2)) + ".");
print("Or you can buy " + str(qtdGalao) + " gallons, then will cost $ " + str(round(valueGalao,2)) + ".");
print("But if you want economize, you can buy " + str(qtdLata -1 ) + " tin, and " + str(galaoEnco));
print("---------------------------------------------")
print("The liter of ink in tin is $ " + str(round(valorPLata , 2)) + ".");
print("The liter of ink in gallon is $ " + str(round(valorPGalao, 2)) + ".");



