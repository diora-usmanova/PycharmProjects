# FUTURE INVESTMENT VALUE:
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    amount = eval(input("The amount Invested for 30 years : "))
    rate = eval(input("Annual interest rate: "))
    print("Years        Future value ")

    monthlyInterestRate = rate / 1200
    for years in range(1, 31):
        futureInvestmentValue = amount * (1 + monthlyInterestRate) ** (years * 12)
        print(years, format(futureInvestmentValue, ">20.2f"))


futureInvestmentValue('investmentAmount', 'monthlyInterestRate','years')
