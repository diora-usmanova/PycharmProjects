investmentAmount = eval(input("Enter investment amount:"))
annualInterestRate = eval(input("Enter annual Interest rate : "))
monthlyInterestRate = annualInterestRate / 1200
years = eval(input("Enter a number of years: "))
numberOfMonth = years * 12
futureInvestmentvalue = investmentAmount * (( 1+ monthlyInterestRate) ** numberOfMonth)
print("Accumulated Value is ", futureInvestmentvalue)