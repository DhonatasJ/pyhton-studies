# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso 
# deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar 
# o número com ou sem o traço separador.
import re
nmr = input("Insira o numero: ")

nmrClean = nmr.replace("-", "")
def cleanNmr(nmrClean):
    nmrCorrija = ""
    if len(nmrClean) == 7:
        nmrCrt = "7" + nmrClean
        print(nmrCrt)
    else:
        print("Numero invalido!") 

cleanNmr(nmrClean)