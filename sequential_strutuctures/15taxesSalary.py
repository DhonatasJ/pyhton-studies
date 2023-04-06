valueEarn = float(input("Enter how much do you earn per each hour:"));
hoursWorked = int(input("Enter how many days you worked per month: "));
salary = valueEarn * hoursWorked;
ir = (salary / 100) * 11;
inss = (salary / 100) * 8;
sindicato = (salary / 100) * 5;
liquidSalary = (salary - (ir + inss + sindicato));
print("Your monthly salary is R$ "+ str(round(salary, 2)));
print("You will pay R$ " + str(round(ir, 2)) + " of tax IR.");
print("You will pay R$ " + str(round(inss, 2)) + " of tax INSS.");
print("You will pay R$ " + str(round(sindicato, 2)) + " of tax Sindicato.");
print("Your liquid salary is R$ " + str(round(liquidSalary, 2)) + ".")



