# SUM THE MAJOR DIOGANAL IN MATRIX
def main():
    m = []

    for j in range(1, 5):
        row = [float(item) for item in input("Enter 4-by-4 matrix row for row  " + str(j) + ":").split()]
        m.append(row)
        j += 1

    major_diagonal = sum(m[i][i] for i in range(len(m)))

    print("Sum of the elements in the major diagonal is ", major_diagonal)

main()



# COMPUTE THE HOURS FOR EVERY EMPLOYEE
def main():
    hours = [
        [2, 4, 3, 4, 5, 8, 8],
        [7, 3, 4, 3, 3, 4, 4],
        [3, 3, 4, 3, 3, 2, 2],
        [9, 3, 5, 7, 3, 2, 2],
        [3, 5, 4, 3, 6, 3, 8],
        [3, 4, 4, 6, 3, 4, 4],
        [3, 7, 4, 8, 3, 8, 4],
        [6, 3, 5, 9, 2, 7, 9]]

    newList = []
    for row in range(len(hours)):
        total = 0
        for column in range(len(hours[0])):
            total += hours[row][column]

        newList.append(total)

    newList.sort(reverse=True)

    for item in range(len(newList)):
        print("Total hours of Employee ", item, "is", newList[item])
main()

# LOCATE THE LARGEST ELEMENT
def main():
    matrix = []

    numRows = eval(input("Enter the number of rows in the list: "))
    for i in range(numRows):
        row = [float(item) for item in input ("Enter a row: ").split()]
        matrix.append(row)

    locateLargest(matrix)


def locateLargest(a):
    maxElem = 0
    indexOfMaxrow = 0
    indexOfmaxColumn = 0
    for i in range(len(a)):
        maxElemInRow = max(a[i])
        if(maxElemInRow > maxElem):
            maxElem = maxElemInRow
            indexOfMaxrow = i
            indexOfmaxColumn = a[i].index(maxElemInRow)
    print("The location of the largest element is at ","(", indexOfMaxrow,",", indexOfmaxColumn, ")")


main()
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


# ADD TWO MATRICES
def main():
    matrix1 = []
    a = 0
    matrix1 = []
    a = 0
    num1 = input("Enter matrix1 :").split()
    lst1 = [float(x) for x in num1]
    for row in range(3):
        matrix1.append([])
        for column in range(3):
            matrix1[row].append(lst1[a])
            a += 1
    print(matrix1)

    matrix2 = []
    b = 0
    num2 = input("Enter matrix2 :").split()
    lst2 = [float(x) for x in num2]
    for row in range(3):
        matrix2.append([])
        for column in range(3):
            matrix2[row].append(lst2[b])
            b += 1
    print(matrix2)

    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    for k in result:
        print("The matrix are added as follows : ", k)


main()

