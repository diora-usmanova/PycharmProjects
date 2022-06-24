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
