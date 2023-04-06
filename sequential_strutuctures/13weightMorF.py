h = float(input("Enter your height: "));
gender = input("Enter your gender, just type M or F: ")
idealWeightM = (72.7*h) - 58;
idealWeightF = (62.1*h) - 44.7;
idealWeight = 0;

if(gender == "F"):
    idealWeight = idealWeightF
elif (gender == "M"):
    idealWeight = idealWeightM
else:
    idealWeight = "invalid gender!"

print("Your ideal weight is " + str(round(idealWeight, 2)));
