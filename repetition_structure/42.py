inter0_25 = []
inter26_50 = []
inter50_75 = []
inter76_100 = []

number = int(input("Insira um numero de 0 a 100: "))
for i in range(number + 1):
    if i >= 0 and i <= 25:
        inter0_25.append(i)
    if i >= 26 and i <= 50:
        inter26_50.append(i)
    if i >= 51 and i <=75:
        inter50_75.append(i)
    if i >= 76 and i <= 100:
        inter76_100.append(i)
print({f"No intervalo de 0 a 25 temos {inter0_25}"})    
print({f"No intervalo de 26 a 50 temos {inter26_50}"})    
print({f"No intervalo de 51 a 75 temos {inter50_75}"})    
print({f"No intervalo de 76 a 100 temos {inter76_100}"})    
