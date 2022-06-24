import random
num1 = random.randint(0,100)
num2 = random.randint(0, 100)
answer = eval(input("What is the " + str(num1)+ "+" + str(num2)+"?"))
print(num1, "+", num2,"=", answer, "is", num1+num2 == answer)
