# SUM ELEMENTS COLUMN BY COLUMN
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
