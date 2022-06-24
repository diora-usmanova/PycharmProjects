# CONVERT INTO CELCIUS(1)
'''celsius = eval(input("Enter a degree in Celsius : "))
fahren = (9/5) * celsius +32
print(celsius, "Celsius is ", fahren, "Fahrenheit")'''

# CONVERT INTO CELCIUS(2)
print("Celsius     Fahrenheit  |  Fahrenheit            Celsius")
fahrenheit = 120.0
for i in range(40, 30, -1):
    fahr = (9/5) * i +32
    print(float(i), format(fahrenheit,">15.2f"), "   |  ", fahrenheit,
          format((5 / 9) * (fahrenheit - 32), ">20.2f"))
    fahrenheit -= 10
