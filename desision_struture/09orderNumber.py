x = int(input("Enter the first number: "));
y = int(input("Enter the second number: "));
z = int(input("Enter the third number: "));

allNumbers = [x, y, z];
desc = sorted(allNumbers, reverse=True);
print(desc);