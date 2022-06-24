def sumRow(m, rowIndex):
    sum = 0
    for i in range(len(m[rowIndex])):
        sum += m[rowIndex][i]


        print("Sum of the elements for row",
 row, "is", sum)

m = []
for j in range(3):
    row = [float(item) for item in input("Enter matrix elements ").split()]
    m.append(row)
    j += 1

sumRow()

