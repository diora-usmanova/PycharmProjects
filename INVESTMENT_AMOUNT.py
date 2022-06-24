#INVESTMENT_AMOUNT
final_amount = eval(input("Enter final amount : "))
interest_rate = eval(input("Enter annual interest rate in percent: "))
monthly_interest = interest_rate / 1200
years = eval(input("Enter number of years : "))
month = years * 12
initialDeposit = final_amount / (1 + monthly_interest) ** month
print("Initial deposit value is", initialDeposit)