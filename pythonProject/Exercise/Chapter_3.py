'''num = 10
num = "Hello"
num = 'Python'
num = 10.45
print(type(num))'''

import math
'''radius = eval(input("Enter a radius"))
area = math.pow(radius, 2)* math.pi
print(area)'''

'''radius = input("Enter a radius")
print(type(radius))
area = float(radius) ** 2 * math.pi
print("The area of the circle is ", area)'''


'''print(format(5621.985372, '10.3f'))
print(format(5621.985372, '<10.3f'), end = '')
print(format(5621.985372, "10f"))
print(format("Hello ", '>10s'))'''

import turtle
'''turtle.begin_fill()
turtle.color("blue")
turtle.circle(100, steps = 4)'''

#turtle.end_fill()

#turtle.circle(100, extent = 180)

'''turtle.begin_fill()
turtle.circle(100)
turtle.color("red")
turtle.end_fill()
turtle.done()'''



#JANUARY 27/2021
'''b = True
print(int(b))
print(type(b))
print(bool(20))'''

'''b= 3>5
print(b)'''

#RANDOM in Python
import random
#num1 = random.randint(0,10)
#num2 = random.randrange(0,10)
#num3 = random.random() # [0,1)
'''num2 = random.randint(0,10)
responce =eval( input("enter the answer of " + str(num1) + "+"\
       + str(num2) + "?"))
print(responce == num1+num2)'''

# IF FUNCTION
'''a = 9
if a > 10:
  print("Hello")
  print("Bye")
else:
    print("Python")
    print("Thank you")'''

# PASS keyword
'''a=3
if a > 8:
    pass
else:
   print("Hello")'''

# REMAINDER function
''' a = 12
if a % 5 == 0:
    print("Hi Five")
if a % 2 ==0 :
    print("Hi Even")'''

'''num1 = random.randint(0,9)
num2= random.randint(0,9)
if num1< num2:
    num1,num2 = num2,num1'''

'''response = eval(input("What is " ,num1,"-",num2,"?"))
if response == num1-num2:
    print("Correct")
else:
    print("Incorrect")'''

'''print("smith\exam1\test.txt")
print("smith\\exam1\\test.txt")
print("smith\"exam1\"test.txt")'''

'''print(math.radians(30) * 6)
print(math.sin(math.pi / 6))
print(chr(97))
print(ord('z') - ord('a'))
print("A", end = ' ')
print("B", end = ' ')
print("C", end = ' ')
print("D")
print(("Chapter"+ str(1)))'''

'''even = False
if even:
    print("It is even!")'''

'''income = 4001
if income > 3000:
    print("Income is greater than 3000")
elif income > 4000:
    print("Income is greater than 4000")


# (ch >= 'A' and ch >= 'Z')
 #print((ch >= 'A' and ch <= 'Z'))
print((ch >= 'A' or ch <= 'Z'))
print(('A' <= ch <= 'Z'))


x - 2 <= 4 and x - 2 >= 4
x - 2 <= 4 and x - 2 > -4
x - 2 <= 4 and x - 2 >= -4
x - 2 <= 4 or x - 2 >= -4

ch = 'F'
if ch >= 'A' and ch <= 'Z':
    print(ch)

x = 0
y = 10 if x > 0 else -10'''

'''count = 0
while count < 10:
    print("Welcome to Python")
    count += 1'''

'''x = 0
while x < 4:
  x = x + 1
print("x is", x)'''

'''sum = 0
for d in range(0, 10, 0.1):
    sum += sum + d'''

'''for i in range(1, 11):
    print(i, end = " ")'''

'''y = 0
for i in range(0, 10):
    y += i
print(y)'''

'''y = 0
for i in range(0, 10, 2):
    y += i
print(y)'''

'''y = 0
for i in range(10, 1, -2):
    y += i
print(y)'''

'''for i in range(1, 6 + 1):
    for j in range(6, 0, -1):
       print(j if j <= i else " ", end = " ")
    print()'''

'''sum = d = 0
while d != 10.0:
    d += 0.1
    sum += sum + d'''

'''for i in range(10):
    for j in range(10):
        print(i * j)'''
'''sum = 0
item = 0
while item < 5:
    item += 1
    sum += item
    if sum >= 4: continue

print(sum)'''









'''sum = 0
item = 0
while item < 5:
    item += 1
    sum += item
    if sum >= 4: continue

number = 25
isPrime = True
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break

print("i is", i, "isPrime is", isPrime)




x = 0
while x < 4:
    x = x + 1

print("x is", x)


















defnPrintln(message, n):
for i in range (0,n)
print(message)



















import random
a = 50
if a > 10:
    pass
print("Hello")
if a % 2 == 0:
    print("Hi even")'''
#num1 = random.randint(0,9)
#num2 = random.randint(0.9)
#if num1 < num2:
 #   num1, num2  = num2,num1
 #   response = eval(input("What is ("num1"),  " ",( num2) "?"))

# from random import randint
'''lotto  = randint(10,99)
guess = eval(input("Guess : "))
lotto1 = lotto % 10
lotto2 = lotto // 10
guess1 = guess % 10
guess = guess // 10

if lotto == guess:
    print("10000$")
elif lotto1 == guess2 and lott2 == guess1:
    print("30000")
elif lotto1 = guess

count = 0
while count < 10:
    print("Hello")
    count += 

for i in range(0,10):
    print(i)
    print("Hello")
    print("bye")'''

s = {"red", "yellow", "green"}
#s.remove("black")
'''print(s)

s1 = {1, 2, 4, 3}
s2 = {1, 5, 4, 13}
print(s1 + s2)'''



