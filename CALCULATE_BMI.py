# CALCULATE BMI

weight = eval(input(" Enter weight in pounds :"))
feet  = eval(input("Enter feet : "))
inches = (eval(input("Enter inches: ")))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_FEET = 0.3048
METERS_PER_INCH = 0.0254
WEIGHT_IN_KILOGRAMMS = weight * KILOGRAMS_PER_POUND
HEIGHT_IN_METERS = (feet * METERS_PER_FEET + inches * METERS_PER_INCH)
BMI= WEIGHT_IN_KILOGRAMMS / (HEIGHT_IN_METERS**2)

print("BMI is ", format(BMI, ".2F"))
if BMI < 18.2:
    print("You are Underweight")
elif BMI < 25:
    print("You are Normal")
elif BMI < 30:
    print("You are Overweight")
else:
    print("You are Obese, sorry ")


# CALCULATE ENERGY

water = eval(input("Enter the amount of water in kg "))
init_temper = eval(input("Enter initial temperature: "))
final_temp = eval(input("Enter the final temperature: "))
energy = water *(final_temp - init_temper) * 4184
print("the Energy needed is ", energy)


# CALCULATE TIPS

subtotal, gratuityRate = eval(input("Enter the subtotal and gratuity rate : "))
gratuity = subtotal * (gratuityRate / 100)
total = subtotal + gratuity
print ("The gratuity is ", gratuity, " and the total is ", total)


 # CHARCHTERS OF ASCII

'''code = eval(input("Enter a ASCII code :"))
print("character is ", chr(code))

character = input("Enter a character: ")
print("the code is ", ord(character))'''

#find the characters fro ! to ~ , 10 characters per line



