import math

r = float(input('Enter the radius measurement: '));
c = 2 * math.pi * r;
roundC = round(c, 3)
print("The circle measure is: " + str(roundC));