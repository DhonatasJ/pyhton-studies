valueHour = float(input("Enter the value earned per hour: "));
hoursWorked = float(input("Enter the hours worked per month: "));
salary = valueHour * hoursWorked;
ir = 0;
inss = (salary / 100) * 10;
fgts = (salary / 100) * 11;
taxesSum = ir + inss + fgts;
salaryLiquid = salary - taxesSum;
if salary <= 900:
    ir = 0
elif salary > 900 and salary <= 1500:
    ir = (salary / 100) * 5
elif salary > 1500 and salary <= 2500:
    ir = (salary / 100) * 10
else:
    ir = (salary / 100) * 20

print("O seu salário bruto é de  R$ " + str(salary));
print("O valor a ser cobrado de IR será de R$ " + str(ir));
print("O valor do INSS a ser cobrado será de R$ " + str(inss));
print("O valor FGTS a ser cobrado será de R$ " + str(fgts));
print("O seu salário liquido é de R$ " + str(salaryLiquid));


