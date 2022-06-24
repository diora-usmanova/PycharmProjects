# COUNT OCCURRENCE OF NUMBERS

numbers = input("Enter the numbers : ")
listOfNumbers = numbers.split()
numberList = [int(x) for x in listOfNumbers]

d1 = {}
for item in numberList:
    if d1.get(item) is None:
        d1[item] = 1
    else:
        d1[item] += 1
l2 = [[y, x] for (x, y) in d1.items()]
l2.sort(reverse=True)
print(l2)
print("Number", l2[0][1], "appear", l2[0][0], "times")

for i in range(0, len(l2) - 1):
    if l2[i][0] == l2[i + 1][0]:
        print("Number", l2[i + 1][1], "appear", l2[i + 1][0], "times")
    else:
        break


# REVERSE A LIST
List = eval(input("Enter a list : "))
print(List)


def Reverse( List):
    return [x for x in reversed(List)]


print("Updated list", Reverse(List))


# COUNT SINGLE DIGITS
import random
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
randomList = []
for i in range(0, 1000):
    n = random.randint(0, 9)
    randomList.append(n)

for i in range(1000):
    if randomList[i] == 0:
        count[0] += 1
    elif randomList[i] == 1:
        count[1] += 1
    elif randomList[i] == 2:
        count[2] += 1
    elif randomList[i] == 3:
        count[3] += 1
    elif randomList[i] == 4:
        count[4] += 1
    elif randomList[i] == 5:
        count[5] += 1
    elif randomList[i] == 6:
        count[6] += 1
    elif randomList[i] == 7:
        count[7] += 1
    elif randomList[i] == 8:
        count[8] += 1
    else:
        count[9] += 1

for i in range(10):
    print("Number of ", i, "'s are ", count[i])

