# STUDENTS SCORE
'''f = open('Score_textFile', 'r')
Scores = f.read()
print(Scores)
s = set()
items = Scores.split()
s = set(str(x) for x in items)
print(s)

f.close()'''


# FIND THE HIGHEST SCORE

highest_score = 0
second_highest = 0
num_students = eval(input("Enter the number of student"))
for i in range(num_students):
    score = eval(input("Enter the score for student each student: "))
    if score > highest_score:
        second_highest = highest_score
        highest_score = score
print("Highest Score is", highest_score)
print("Second highest score is " , second_highest)


#SPLIT_DIGITS
number = eval(input("Enter an integar: "))
num1 = number // 1000
num2 = (number % 1000) // 100
num3 = (number % 100) // 10
num4 = number % 10
print(num1)
print(num2)
print(num3)
print(num4)


# SUM A SERIES
sum = 0
for i in range(1,98,2):
    sum += i/(i+2)
print(sum)


# SUM DIGITS OF AN INTEGAR

def sumDigits(n):
    sum  = 0
    while n != 0:
        sum = sum + n % 10
        n = n // 10
    return sum

def main():

    n= eval(input("Enter an integar"))
    print(sumDigits(n))
main()


# INTEGAR REVERSED
def reverse(number):
    reverse_number = 0
    while(number>0):
        remainder = number % 10
        reverse_number= (reverse_number*10)+ remainder
        number = number // 10
    print(reverse_number)
reverse(1234)


