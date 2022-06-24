# POUND TO KILOS
pounds = eval(input("entera value in pounds"))
kilos = pounds*0.454
print(pounds, "pounds is ", kilos, "kilograms")'''

# KOLOGRAM TO POUNDS
 print("Kilogramms        Pounds")
for i in range(1, 200):
    print(i, format(i * 2.2, ">22.1f"))'''

print("Kilogramms        Pounds   |     Pounds        
 Kilogramms")
pounds = 20
for i in range(1, 200, 2):
    print(i, format(i * 2.2, ">20.2f"), "    |", pounds, 
 format(pounds * 0.4545, ">25.2f"))
    pounds +=5


# FROM MILES TO KM, FROM KM TO MILES

print("miles       kilometers    |     kilometers     
      miles")
kilometers = 20
for i in range(1, 11):
    print(i, format(i * 1.609, ">20.3f"), "   |     ",
 kilometers, format(kilometers * 0.621, ">23.3f"))
    kilometers += 5


# CURRENCY EXCHAGE
rate = eval(input("Enter the exchange rate: "))

convert = eval(input("Enter 0 to convert to dollars
 and 1 to vice versa: "))
if convert == 0:
    print("Enter the dollar amount: ")
    dollar_amount = eval(input())
    exch_to_dollar = dollar_amount * rate
    print(dollar_amount, " dollar is ", format(exch_to_dollar,".2f"), 
" foreign currency")
elif convert == 1:
    print("Enter a foreigh currency amount")
    curr_amount = eval(input())
    exch_to_foreign = curr_amount / rate
    print(curr_amount, " foreign currency is ", format(exch_to_foreign,".2f"),
 "dollars")
else:
    print("Incorrect input")


#DECIMAL TO HEX
value = eval(input("Enter a value between 0 and 15: "))
if value in range(0,16):
    print("The hex value is ", hex(value))
else:
    print("invalid Input")

# FIND THE SMALLEST N
'''n = 1
while n**2 <= 12000:
    n += 1
print(n)'''


# find the largest n
n = 1
while pow(n, 3) <= 1200:
    n += 1
print(n)






