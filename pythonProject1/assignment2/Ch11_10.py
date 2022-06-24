# LARGEST ROW AND COLUMNS
import random

m = []
for i in range(4):
    row = []
    for j in range(4):
        num = random.randint(0, 1)
        row.append(num)
    m.append(row)
for row in m:
    for element in row:
        print(element, end=' ')
    print()

largest_row = 0
sum = 0
for i in range(len(m)):
    if m[i].count(1) >= sum:
        sum = m[i].count(1)
        largest_row = i

largest_column = 0

for column in range(len(m[0])):
    sum = 0
    for row in range(len(m)):
        sum += m[row][column]
        if m[column].count(1) >= sum:
            sum = m[column].count(1)
            largest_column = column

print("largest row index  ", largest_row)
print("largest Column index", largest_column)
