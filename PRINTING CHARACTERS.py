#PRINTING CHARACTERS
#def printChars(ch1,ch2,numberPerLine):
CHARACTERS_PER_LINE = 10
total = 1
char1 = chr(1)
char2 = chr(90)
print("Charachters from", char1, "to", char2)
for i in range(1,50):
    total += 1
    if total % CHARACTERS_PER_LINE ==0:
        print()
    print(char1, char2, end =' ')


#printChars('ch1', 'ch2', 'numberPerLine')


