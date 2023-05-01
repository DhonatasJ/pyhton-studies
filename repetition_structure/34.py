num = int(input("Insira um numero inteiro: "));
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print("O numero inserido não é um numero primo, tente novamente...")
        break
else:
    print("O numero inserido é um numero primo.")