# ASSIGNING GRADES
score = []
scores = input("Enter scores : ")
items = scores.split()
score = [eval(x) for x in items]
best = max(score)
letter_score = []
for i in range(0, len(score)):
    if score[i] >= best - 10:
        letter_score.append('A')
    elif score[i] >= best - 20:
        letter_score.append('B')
    elif score[i] >= best - 30:
        letter_score.append('C')
    elif score[i] >= best - 40:
        letter_score.append('D')
    else:
        letter_score.append('F')

for j in range(len(score)):
    print("Student ", j, "score is", score[j], "and grade is ", letter_score[j])
