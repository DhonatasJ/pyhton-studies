letters = []
consoantes = []
for i in range(10):
    lts = input("Insira uma consoante ")
    letters.append(lts)
for i in letters:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        x = i
        consoantes.append(x)
print(f"Foram lidas {len(consoantes)} consoantes")
print(consoantes)
