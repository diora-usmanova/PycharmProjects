from random import randint
def printMatrix(n):
   for i in range (n):
        for j in range(n):
            number = randint(0,1)
            print(number, end=" ")
        print("")
n = int(input("Enter n: "))
printMatrix(n)

