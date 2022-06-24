# COMPOUND VALUE
'''amount = eval(input("Enter the amount : "))
annual_interest = eval(input("Enter the annual 
interest rate :"))
month = eval(input("Enter the month : "))
monthly_interest = annual_interest / 1200
monthly_increase = amount * (1 + monthly_interest)
sum = 0
for i in range(1, month + 1):
    sum = (amount + sum) * (1 + monthly_interest)
print(format(sum, "5.3f"))'''


# COMPUTE CD VALUE
amount = eval(input("Enter the amount: "))
apy = eval(input("Enter the APY: "))
month = eval(input("Enter the month: "))
monthly_apy = apy / 1200
monthly_increase = amount + amount * apy / 1200
sum =0
for i in range(1, month+1):
    sum = monthly_increase
    print(i,"   ",  format(monthly_increase, "7.2f"))
    monthly_increase= monthly_increase +
 monthly_increase * monthly_apy


# CONVERT INTO CELCIUS(1)
'''celsius = eval(input("Enter a degree in Celsius : "))
fahren = (9/5) * celsius +32
print(celsius, "Celsius is ", fahren, "Fahrenheit")'''

# CONVERT INTO CELCIUS(2)
print("Celsius     Fahrenheit  |  Fahrenheit        
    Celsius")
fahrenheit = 120.0
for i in range(40, 30, -1):
    fahr = (9/5) * i +32
    print(float(i), format(fahrenheit,">15.2f"), "   |  ",
 fahrenheit,
          format((5 / 9) * (fahrenheit - 32), ">20.2f"))
    fahrenheit -= 10


# FROM FEET TO METERS
'''foot = eval(input("Enter a value for feet : "))
meter = foot * 0.305
print(foot, " feet is ", meter, "meters" )'''


# FROM MILES TO KILOMETERS
'''print("Miles            Kilometers")
for i in range(1,11):
    print(i, format(i * 1.609, ">23.3f"))'''



# FROM MILES TO KM, FROM KM TO MILES
print("miles       kilometers    |     kilometers           miles")
kilometers = 20
for i in range(1, 11):
    print(i, format(i * 1.609, ">20.3f"), "   |     ", kilometers, format(kilometers * 0.621, ">23.3f"))
    kilometers += 5

