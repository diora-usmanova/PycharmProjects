# ANALIZE THE SCORE
score = []
scores = input("Enter scores : ")
items = scores.split()
score = [eval(x) for x in items]
average = sum(score) // len(score)

count = 0
for i in range(len(score)):
    if score[i] >= average:
        count += 1
Count = 0
for j in range(len(score)):
    if score[j] < average:
        Count += 1
print("Average is : ", average)
print("Above average is : ", count)
print("Below average is: ", Count)


# REVERSE THE NUMBER ENTERED

def reverse(s):
    return s[:: -1]
s = []
s = reverse(input("Enter integers : "))
print(s)


SUM ELEMENTS COLUMN BY COLUMN
def sumColumn(m, columnIndex):
    for column in range(len(m[0])):
        total = 0
        for row in range(len(m)):
            total += m[row][column]
        print("Sum of the elements for column",
 column, "is", total)

m = []
for j in range(3):
    row = [float(item) for item in input("Enter 3-by-4 
matrix row for row  " + str(j) + ":").split()]
    m.append(row)
    j += 1

sumColumn(m, 0)


# GCD
numbers = []
num = input("Enter 5 numbers : ")
items = num.split()
numbers = [eval(x) for x in items]
print(numbers)


def gcd(numbers):
    gcd = 1
    k = 2
    while k <= numbers[0] and k <= numbers[-1]:
        if numbers[0] % k == 0 and numbers[-1] % k == 0:
            gcd = k
        k += 1
    return gcd


print(gcd(numbers))

