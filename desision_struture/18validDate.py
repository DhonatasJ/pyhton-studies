from datetime import datetime
date = input("Please, insert a date in dd/mm/yyyy format ");
def verifyDate(date):
    try:
        datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

if verifyDate(date):
    print("Is a valid date")
else:
    print("Is a invalid date")