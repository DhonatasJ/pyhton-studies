# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Insira uma frase: ")

def conteStr(frase):
    have = []
    haveSpace = []
    vogais = ["a","e","i","o","u"]
    for i in frase:
        if i in vogais:
            have.append(i)
    for i in frase:
        if i in [" "]:
            haveSpace.append(i)
            print(len(haveSpace))
    print(f"As vogais a, e, i, o, u, aparecem {len(have)} vezes")
    print(f"Sua frase contem {len(haveSpace)} espaços em branco")

conteStr(frase)