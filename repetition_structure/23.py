n = int(input("Insira um número inteiro: "))
count_divisoes = 0
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        count_divisoes += 1
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
print("Número de divisões executadas:", count_divisoes)
