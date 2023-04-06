hours, minutes = input("Enter hours worked for day in hh:mm format: ").split(':');
salaryMonth = float(input('Enter how much you earn per month: '));
daysWorked = int(input("Enter how much days do you work: "));
timeInFloat = hours + '.' + minutes;
convertTime = float(timeInFloat);
x = daysWorked * convertTime;
y = salaryMonth / x;
print(round(y, 2));

