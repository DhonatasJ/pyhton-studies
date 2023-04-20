strawberrykg = float(input("Insert how many strawberry kilos you want: "));
applekg = float(input("Now, insert how many apple kilos you want: "));

strawberryL5 = 2.5;
strawberryG5 = 2.2;
appleG5 = 1.8;
appleL5 = 1.5;

def strawberry(strawberrykg,strawberryL5,strawberryG5):
    if strawberrykg <= 5:
        discL = strawberrykg * strawberryL5
        return discL;
    elif strawberrykg > 5:
        discG = strawberrykg * strawberryG5
        return discG;

def apple(applekg,appleL5,appleG5):
    if applekg <= 5:
        discL = applekg * appleL5
        return discL;
    elif applekg > 5:
        discG = applekg * appleG5
        return discG;

if (strawberrykg + applekg) < 25:
    print("Strawberry R${:.2f}".format(strawberry(strawberrykg,strawberryL5,strawberryG5)))
    print("Apple R${:.2f}".format(apple(applekg,appleL5,appleG5)))
elif (strawberrykg + applekg) >= 25:
    x = (strawberry(strawberrykg,strawberryL5,strawberryG5) + apple(applekg,appleL5,appleG5))
    y = x - ((x / 100) * 10)
    print("Strawberry R${:.2f}".format(strawberry(strawberrykg, strawberryL5, strawberryG5)))
    print("Apple R${:.2f}".format(apple(applekg, appleL5, appleG5)))
    print("Because the value is R${:.2f}".format(x) + " we will give a 10% discount and the value will be R${:.2f}".format(y))
