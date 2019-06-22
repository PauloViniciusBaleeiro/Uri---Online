salary = input()
salary = float(salary)

if salary <= 2000.00:
    print("Isento")

elif salary <= 3000.00:
    tax = (salary-2000.00) * 0.08
    print ("R$ {0:.2f}".format(round(tax, 2)))

elif salary <= 4500.00:
    base = (salary - 3000.00)
    tax = (base * 0.18) + (1000.00 * 0.08)
    print ("R$ {0:.2f}".format(round(tax, 2)))

elif salary > 4500.00:
    base = (salary - 4500)
    tax = (base * 0.28) + (1000.00 * 0.08) + (1500.00 * 0.18)
    print ("R$ {0:.2f}".format(round(tax, 2)))
