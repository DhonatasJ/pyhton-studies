import random
def embaralha(word):
    nrand = random.randint(1,2)
    if nrand  == 1:
        word = word.upper()
    else:
        word = word.lower()

    wordX = list(word)
    random.shuffle(wordX)
    wordRand = "".join(wordX)
    return wordRand

    
word = input("Insira uma palavra: ")
print(embaralha(word))