#HEADS AND TAILS
import random
num = random.randint(0,1)
answer = eval(input("Enter a number 0 or 1 :"))
if num == answer:
    print("Correct")
else:
    print("Wrong")
count_heads = 0
count_tails = 0
num = random.randint(0,1000000)
for num in range (num):
    if num % 2 == 0:
        count_heads+=1
    else:
        count_tails += 1
print("Number  of heads :", count_heads)
print("Number of tails: ", count_tails)







