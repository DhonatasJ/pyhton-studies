while True:
    name = input("Insert your user: ");
    password = input("Insert your password: ");

    if name != password:
        print("Logging in...")
        break
    else:
        print("You cannot use the user as a password, please try again...")