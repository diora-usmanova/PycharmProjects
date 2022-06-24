# ADDING NUMBERS

import random
'''num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
answer = eval(input("What is " + str(num1) + 
"+" + str(num2) + "+ " + str(num3)+"?"))
print(num1,"+", num2, "+", num3 , "=", 
answer, "is", num1+num2+num3 == answer)'''


# LEARNING ADDITION


'''for i in range (0,6):
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    answer = eval(input("What is " + str(num1) +
 "+" + str(num2) + "?"))
    print(num1,"+", num2,  "=", answer, "is",
 num1+num2 == answer)'''


# LEARNING SUBSTRACTION

for i in range (0,6):
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    if num1 < num2:
        num1, num2 = num2,num1
    answer = eval(input("What is "+ str(num1) +
 "-" + str(num2) + "?"))
    if num1 - num2 == answer:
        print(num1,"-", num2,  "=", answer, 
"is", num1-num2 == answer)
    else:
        print("You are wrong, correct answer is ",
 num1 - num2)


# AREA OF HEXAGON
s = eval(input("Enter a side :"))
area = ((3* (3 ** 0.5)) * s**2) / 2
print("area of hexagon is ", area)
 

# AREA OF PENTAGON
import math
length = eval(input("Enter the length: "))
PI = 3.14159
s = 2*length * (math.sin(PI/ 5))
area = ((3 * 3**0.5) * s ** 2) / 2
print("The area of pentagon is ", area)

