str1 = input("Insira uma palavra ou frase para a comparacao: ")
str2 = input("Insira outra palavra ou frase para a comparacao da primeira: ")


def string(str1, str2):
    if len(str1) != len(str2):
        difLen = "diferentes"
    else: 
        difLen = "iguais"

    if str1 != str2:
        dif = "diferente"
    else: 
        dif = "igual"

    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print(f"Tamanho de \"{str1}\": {len(str1)} caracteres")
    print(f"Tamanho de \"{str2}\": {len(str2)} caracteres")
    print(f"As duas strings são de tamanhos {difLen}")
    print(f"As duas strings possuem conteúdo {dif}")

string(str1, str2)