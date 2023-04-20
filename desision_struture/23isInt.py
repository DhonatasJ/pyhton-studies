num = float(input("Please, type a number: "));
numRound = round(num)
x = num % numRound;

if x == 0:
    print("Integer");
else:
    print("Decimal");