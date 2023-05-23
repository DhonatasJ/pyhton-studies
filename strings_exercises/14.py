to_change = {
    "a":"4",
    "e":"3",
    "i":"1",
    "l":"1",
    "o":"0",
    "s":"5",
    "t":"7",
}
new_word = ""
word = input("Insert a word, for change to Leet Speak: ")

def change(word, to_change, new_word):
    for letra in word:
          if letra in to_change:
              new_word += to_change[letra]
          else:
              new_word += letra
    return new_word

result = change(word,to_change,new_word)
print(result)