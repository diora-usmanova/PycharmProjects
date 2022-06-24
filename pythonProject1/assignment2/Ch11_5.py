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
