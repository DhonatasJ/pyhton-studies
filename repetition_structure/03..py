def validLogin(name, age, salary, gender, maritalStatus):
    return True if len(name) > 3 else False;
    return True if age >= 0 and age <= 150 else False;
    return True if salary > 0 else False;
    return True if gender == "f" or "m" else False;
    return True if maritalStatus == "s" or "c" or "v" or "d" else False;
while True:
    name = input("Name: ");
    age = int(input("Age: "));
    salary = float(input("Salary: "));
    gender = input("Gender: ");
    maritalStatus = input("Marital Status: ");
    if validLogin(name, age, salary, gender, maritalStatus) == True:
        print("OK!")
        break
    else:
        print("Invalid data, please try again...")
