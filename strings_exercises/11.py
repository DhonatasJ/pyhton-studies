# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto 
# e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

palavra = "arroz"

def jogo_da_forca(palavra):
    palavra_crt = ""
    for i in range(6):
        cada_letra = ""
        letra = input(f"A palavra contem {len(palavra)} letras, insira uma: ")
        cada_letra += letra
        for i in palavra:
            print("Voce acertou, uma letra, continue...")
            palavra_crt = input("Insira uma palavra : ")
            if palavra_crt == palavra:
                print("Acertou!")
                return
            else:
                print("Voce errou!")
                letra = input(f"Insira outra letra: ")
                palavra_crt += letra
jogo_da_forca(palavra)