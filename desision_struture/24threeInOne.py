x = float(input("Please, insert a number: "));
y = float(input("Please, insert other number: "));
print(f"Nice, the chosen numbers was {x} and {y}");
choice = int(input("Now chooce the next operation down: \n'1' To even or odd \n'2' To positive or negative \n'3' To integer or decimal \n ANSWEAR "))

def isEvenOrOdd(x,y):
    print(f"{x} is even!") if x % 2 == 0 else print(f"{x} is odd!")
    print(f"{y} is even!") if y % 2 == 0 else print(f"{y} is odd!")

def isPostiveOrNeg(x,y):
    print(f"{x} is Negative" if x < 0 else print(f"{x} is Positive"));
    print(f"{y} is Negative" if y < 0 else print(f"{y} is Positive"));

def isIntOrDec(x, y):
    print(f"{round(x)} is Integer ") if x % round(x) == 0 else print(f"{x} is Decimal")
    print(f"{round(y)} is Integer ") if y % round(y) == 0 else print(f"{y} is Decimal")

if choice == 1:
    isEvenOrOdd(x,y)
elif choice == 2:
    isPostiveOrNeg(x,y)
elif choice == 3:
    isIntOrDec(x,y)
else:
    print("Number choice invalid, try again...")