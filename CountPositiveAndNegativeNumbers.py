# COUNT POSITIVE AND NEGATIVE NUMBERS
'''count_pos = 0
count_neg = 0
total = 0
sum = 0
number = eval(input("Enter an integer , 
the input ends if it is 0: "))

if number == 0:
    print("You did not enter any number ")

while number != 0:
    total += 1
    sum += number
    number = eval(input("Enter an integer , 
it ends if it is 0: "))
    if number > 0:
        count_pos += 1
    if number < 0:
        count_neg += 1

    if number == 0:
        print("The number of positives is ", count_pos)
        print("The number of negatives is ", count_neg)
        print("Total is ", total)
        print("The average is ", sum / total)'''



count_pos = 0
count_neg = 0
total = 0
sum = 0
while True:
    total += 1
    number = eval(input("Enter an integer ,
 it ends if it is 0: "))
    sum += number
    if number > 0:
        count_pos += 1
    elif number < 0:
        count_neg += 1
    elif number == 0:
        print("You did not enter any number ")
        break
print("The number of positives is ", count_pos)
print("The number of negatives is ", count_neg)
print("Total is ", total)
print("The average is ", sum / total)
