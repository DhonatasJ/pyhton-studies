while True:
    num = float(input("Insert a number between 0 and 10: "));

    if num >= 0 and num <= 10:
        print(f"{num} is valid")
        break
    else:
        print(f"{num} is invalid, try again...")


