num = int(input("Insira um numero inteiro: "))
div = [];
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        div.append(i)
if len(div) == 0:
    print("O numero inserido  é um numero primo.")
else:
    print(f"O numero i"
          f"nserido não é um numero primo. Apenas divisiveis por {div}")