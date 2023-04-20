weight = float(input("Enter the weight of fish: "));
overweight = 0;
if (weight > 50):
    overweight = weight - 50;
else:
    overweight = 0;
fees = overweight * 4;

print("The overweight is " + str(round(overweight, 2)) + "KG");
print("You going need to pay about fees R$" + str(round(fees, 2)));
