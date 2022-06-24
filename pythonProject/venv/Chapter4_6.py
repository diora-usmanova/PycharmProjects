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



