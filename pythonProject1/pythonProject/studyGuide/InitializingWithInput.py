matrix = []
for row in range(3):
    matrix.append([])
    for column in range(3):
        value = eval(input("Enter an element :"))
        matrix[row].append(value)

print(matrix)
