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
