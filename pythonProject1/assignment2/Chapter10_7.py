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
