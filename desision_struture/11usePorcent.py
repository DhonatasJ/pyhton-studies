salary = float(input("Please, enter the employees salary: "));
percentage = 0.0;
salaryIncrease = 0.00;
salaryUp = 0.00
if salary <= 280.00:
    percentage = 20;
    salaryIncrease = (salary / 100) * percentage;
    salaryUp = salary + salaryIncrease;
elif salary > 280 and salary < 700:
    percentage = 15;
    salaryIncrease = (salary / 100) * percentage;
    salaryUp = salary + salaryIncrease;
elif salary >= 700 and salary < 1500:
    percentage = 10;
    salaryIncrease = (salary / 100) * percentage;
    salaryUp = salary + salaryIncrease;
else:
    percentage = 5;
    salaryIncrease = (salary / 100) * percentage;
    salaryUp = salary + salaryIncrease;

print("The salary before the readjustment was $" + str(salary));
print("The percentage of applied increase is " + str(percentage) + "%");
print("The value of the increase is $" + str(salaryIncrease));
print("The new salary, after the increase will be $" + str(salaryUp));
