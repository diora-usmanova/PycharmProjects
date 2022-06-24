# PAYROLL
empl = input("enter employee's name : ")
hours_worked = eval(input("Enter a hours: "))
rate = eval(input("Enter hourly rate: "))
fedaral_tax_rate = eval(input("Enter federal tax rate: "))
state_rate = eval(input("Enter state tax rate: "))
gross_pay = hours_worked * rate
fed_tax = gross_pay * fedaral_tax_rate
st_tax = gross_pay * state_rate
total_deductions = fed_tax + st_tax
net_pay = gross_pay - total_deductions
print("Employee name : ", empl)
print("Hours worked ", hours_worked)
print("pay rate  $ ", rate)
print(" Gross pay : ",gross_pay )
print("Federal witholding : ", fed_tax)
print("State withholding: ", st_tax)
print("Net pay",net_pay )

