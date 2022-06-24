numberOfStudents = eval(input("Enter the number of students "))
max_score = -1
for i in range(numberOfStudents):
    score = eval(input("Enter a score of each student"))
    if score > max_score:
        max_score = score
print("Highest score is ",(max_score))





