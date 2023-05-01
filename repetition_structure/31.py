import math
import random
products = random.randint(1,10)
sumvalues = []

for i in range(products):
    randomvl = random.uniform(1, 100)
    print(f"The values of {i+1} items cost R${randomvl:.2f}")
    sumvalues.append(randomvl)
cash = float(input(f"Your purchases cost R${sum(sumvalues):.2f}, insert the payment value: "))
while True:
    if cash > sum(sumvalues):
        print(f"Your change is R${cash - sum(sumvalues):.2f}")
        break
    else:
        while cash < sum(sumvalues):
            rest = float(input(f"Still missing R${sum(sumvalues) - cash:.2f}, please insert the rest: "))
            cash += rest