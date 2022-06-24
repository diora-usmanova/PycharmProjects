def sumColumn(m, columnIndex):
    matrix = []
    numberOfRows = 3
    numberOfColumns = 4
    for row in range(numberOfRows):
        matrix.append([])
        for column in range(numberOfColumns):
            element = input("Enter 3-by-4 matrix row for row 0 :")
            # matrix[row].append(element)
            items = element.split()
            row = [eval(x) for x in items]
        print(matrix)
        return matrix
