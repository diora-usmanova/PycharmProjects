
# SOCIAL SECURITY NUMBER

ssn = input("Enter a social security number: ")
if ssn.isalnum():
    print("Invalid SSN")
else:
    print("Valid SSN")


# COUNTING A CHARACTER IN A STRING

str = input("Enter a string : ")
ch = input("Enter a character: ")

def count(str, ch):
    num = 0
    for i in range(0, len(str)):
        if str[i] == ch:
            num += 1
    return num
print(count(str, ch))



# LONGEST COMMON PREFIX
def prefix(s1, s2):
    s3 = ""
    for a in range(len(s1)):
        if s1[a] == s2[a]:
            s3 = s3 + s1[a]
        else:
            return s3
    return s3


def main():
    s1 = input("Enter first string: ")
    s2 = input("Enter a second string")
    print(prefix(s1, s2))


if __name__ == "__main__":
    main()


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


