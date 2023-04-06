x = int(input("Please, enter a integer number: "));
y = int(input("Enter other please: "));
z = float(input("Enter a real number: "));
calc01 = (x * 2) + (y / 2)
calc02 = x * 3 + z;
calc02Str = str(calc02)
calc02Int = int(calc02)
useCalc02 = 0;
if(calc02Str[-1] == "0"):
    useCalc02 = calc02Int
else:
    useCalc02 = calc02;
calc03 = z ** 3;
calc03Int = int(calc03);
calc03Str = str(calc03);
calc03Use = 0;
if(calc03Str[-1] == "0"):
    calc03Use = calc03Int
else:
    calc03Use = calc03
print("The product double the first with half of the second is " + str(int(calc01)));
print("The sum of the triple of the first with the third is " + str(useCalc02));
print("The third elevated to the cube is " + str(round(calc03Use, 2)));


