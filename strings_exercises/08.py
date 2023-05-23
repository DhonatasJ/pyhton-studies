text = input("Insira o conteudo: ")

def confere(text):
    text = str(text)
    text = text.lower()
    textChange = text.split(" ")
    textChange = "".join(textChange)
    textReverse = textChange[::-1]
    if textChange == textReverse:
        print("A frase é um palíndromo")
    else:
        print("A frase nao é um palíndromo")

confere(text)