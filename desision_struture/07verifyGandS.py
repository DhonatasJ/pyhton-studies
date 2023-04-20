num1 = int(input("Please, enter a first number: "));
num2 = int(input("Please, enter a second number: "));
num3 = int(input("Please, enter a third number: "));
smaller = 0;
bigger = 0;
def is_bigger (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3;

def is_smaller (num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3;

smaller = is_smaller(num1, num2, num3);
bigger = is_bigger(num1, num2, num3);
print("The higher number is " + str(smaller));
print("The higher smaller is " + str(bigger));
