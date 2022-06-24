#DECIMAL TO HEX
value = eval(input("Enter a value between 0 and 15: "))
if value in range(0,16):
    print("The hex value is ", hex(value))
else:
    print("invalid Input")