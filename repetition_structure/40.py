menorInd = float('inf')
maiorInd = 0
media = []
mediaMnrCidade = []
for i in range(5):
    codCity = int(input("Insira o codigo da cidade: "))
    qtdVeicPass = int(input("Insira a quantidade de veiculos de passeio: "))
    acidentes = int(input("Insira a quantidade de acidentes no ano: "))
    media.append(qtdVeicPass)
    if acidentes < menorInd:
        menorInd = acidentes
        codMenor = codCity
    if acidentes > maiorInd:
        maiorInd = acidentes
        codMaior = codMenor
    if qtdVeicPass < 2000:
        x = acidentes
        mediaMnrCidade.append(x)


print('A cidade {} tem o menor indice de acidentes, sendo {} e a cidade {} tem o maior indice sendo {}'.format(codMenor, menorInd, codMaior, maiorInd))
print('A media de veiculos nas cindo cidades juntas é {}'.format(sum(media) / 5))
print('A media de acidentes em cidades com menos de 2000 veiculos é de {}'.format(round(sum(mediaMnrCidade)/ len(mediaMnrCidade)),2))