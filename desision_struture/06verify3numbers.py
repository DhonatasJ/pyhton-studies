num1 = int(input("Please, enter a first number: "));
num2 = int(input("Please, enter a second number: "));
num3 = int(input("Please, enter a third number: "));
if num1 >= num2 and num1 >= num3:
    print("The largest number is " + str(num1))
elif num2 >= num1 and num2 >= num3:
    print("The largest number is " + str(num2))
else:
    print("The largest number is " + str(num3));
