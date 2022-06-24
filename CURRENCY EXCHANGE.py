# CURRENCY EXCHAGE
rate = eval(input("Enter the exchange rate: "))

convert = eval(input("Enter 0 to convert to dollars and 1 to vice versa: "))
if convert == 0:
    print("Enter the dollar amount: ")
    dollar_amount = eval(input())
    exch_to_dollar = dollar_amount * rate
    print(dollar_amount, " dollar is ", format(exch_to_dollar,".2f"), " foreign currency")
elif convert == 1:
    print("Enter a foreigh currency amount")
    curr_amount = eval(input())
    exch_to_foreign = curr_amount / rate
    print(curr_amount, " foreign currency is ", format(exch_to_foreign,".2f"), "dollars")
else:
    print("Incorrect input")

