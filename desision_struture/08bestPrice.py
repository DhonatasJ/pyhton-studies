price1 = float(input("Enter the first product value: "));
price2 = float(input("Enter the second product value: "));
price3 = float(input("Enter the third product value: "));

def bestPrice(price1, price2, price3):
    if price1 >= price2 and price1 >= price3:
        return 1
    elif price2 >= price1 and price2 >= price3:
        return 2
    else:
        return 3;
bestPrice = bestPrice(price1, price2, price3);
print("You should buy the " + str(bestPrice) + "° product.")