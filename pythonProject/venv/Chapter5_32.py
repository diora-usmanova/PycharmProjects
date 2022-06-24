amount = eval(input("Enter the amount : "))
annual_interest = eval(input("Enter the annula interest rate :"))
month = eval(input("Enter the month : "))
monthly_interest = annual_interest / 1200
monthly_increase = amount*(1+monthly_interest)
sum = 0
for i in range(1,month+1):
    sum = (amount + sum)*(1+monthly_interest)
print(sum)
 