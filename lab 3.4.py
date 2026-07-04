#inputs
basic_salary=float(input("enter your basic salary: Rs."))
overtime_hours=float(input("enter your overtime hours:"))
overtime_rate=float(input("enter overtime rate:"))
bonus=float(input("enter your bonus:"))
tax_percentage=float(input("enter tax percentage:"))


#logic
overtime_payment=overtime_hours*overtime_rate
gross_salary=overtime_payment+bonus+basic_salary
tax_amount=gross_salary*(tax_percentage/100)
net_salary=gross_salary-tax_amount

#outputs
print("gross salary: Rs.",gross_salary)
print("tax_amount: Rs.",tax_amount)
print("net_salary: Rs.",net_salary)
                         
