def verify(argument):
    if argument < 0:
        return "N"
    else:
        return "P"
    
argument = float(input("Insert a number: "))
result = verify(argument)
print(result)