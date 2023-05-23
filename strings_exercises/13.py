# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada
# com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se 
# o usuário ganhou ou perdeu o jogo.
import random
palavras = ["Carro", "Feijao", "Chinelo", "Computador", "Tapete", "Pistola", "Academia", "Ventilador", "Fabrica", "Padaria", "Uva", "Policia"]

def advinha(palavras):
    print("ADVINHE UMA DAS PALAVRA ABAIXO, VOCE TERA 6 CHANCES")
    for i in palavras:
        print("---", i)
    n_random = random.randrange(0, len(palavras))
    palavra_random = palavras[n_random]
    print(palavra_random)
    for i in range(6):
        palavra_usuario = input("Tente acertar a palavra: ")
        if palavra_usuario == palavra_random:
            print("Acertou!")
            break
        else:
            print("Palavra incorreta, tente novamente...")
        palavra_usuario = input("Tente acertar a palavra: ")
advinha(palavras)