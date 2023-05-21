#Jogo de Craps.
import random

def craps():
    result = 0
    nums = []
    while True:
        x = input("CLICK \"1\" TO PLAY ")
        if x != "1":
            print("Finished Game!")
            break
        else: 
            rand = random.randint(2,12)
            if rand == 7 or rand == 11:
                print("WIN --- Natural")
                result = rand
                break
            if rand == 2 or rand == 3 or rand == 12:
                print("LOSE --- Craps")
                result = rand
                break
            if rand in [4, 5, 6, 8, 9, 10]:
                print("Ponto...Press \"1\" Again: ")
                result = rand
                while True:
                    rand2 = random.randint(2,12)
                    if rand2 in [4, 5, 6, 8, 9, 10]:
                        result = nums.append(rand2)
                        break
                    else:
                        print("LOSE")
    return result
craps()