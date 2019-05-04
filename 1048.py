salary = input()

salary = float(salary)

if (salary <= 400.00):
    new_salary = salary * 1.15
    print("Novo salario: {0:.2f}".format(round(new_salary, 2)))
    print("Reajuste ganho: {0:.2f}".format(round((new_salary - salary), 2)))
    print("Em percentual: 15 %")

elif(salary <= 800.00):
    new_salary = salary * 1.12
    print("Novo salario: {0:.2f}".format(round(new_salary, 2)))
    print("Reajuste ganho: {0:.2f}".format(round((new_salary - salary), 2)))
    print("Em percentual: 12 %")

elif(salary <= 1200.00):
    new_salary = salary * 1.10
    print("Novo salario: {0:.2f}".format(round(new_salary, 2)))
    print("Reajuste ganho: {0:.2f}".format(round((new_salary - salary), 2)))
    print("Em percentual: 10 %")

elif(salary <= 2000.00):
    new_salary = salary * 1.07
    print("Novo salario: {0:.2f}".format(round(new_salary, 2)))
    print("Reajuste ganho: {0:.2f}".format(round((new_salary - salary), 2)))
    print("Em percentual: 7 %")

else:
    new_salary = salary * 1.04
    print("Novo salario: {0:.2f}".format(round(new_salary, 2)))
    print("Reajuste ganho: {0:.2f}".format(round((new_salary - salary), 2)))
    print("Em percentual: 4 %")
