annualInterestRate = eval(input("Enter annual interest rate :"))
monthlyInterestRate = annualInterestRate / 1200
numberOfYears = eval(input("Enter number of years as an integar : "))
loanAmount = eval(input(" Enter a loan amount : "))
monthlyPayment = loanAmount* monthlyInterestRate / (1-1/ (1+ monthlyInterestRate)** (numberOfYears * 12))
totalPayment = monthlyPayment* numberOfYears* 12
print("The monthly payment is : ", int(monthlyPayment * 100) / 100)
print("The total payment is :  ", int(totalPayment * 100 ) / 100)