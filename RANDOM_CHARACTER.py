# RANDOM CHARACTER

'''import time
randomNumber = int(time.time()) % 26
print(chr(ord('A') + randomNumber))'''

#RANDOM CHARACTER(2)

import RandomCharacter
NUMBER_OF_CHAR = 175
CHAR_PER_LINE = 25
for i in range(NUMBER_OF_CHAR):
    print(RandomCharacter.getRandomLowerCaseLetter(), end = " ")
    if (i + 1) % CHAR_PER_LINE == 0:
        print()


# ROCK , PAPER AND SCISSOR GAME

import random
computer = random.randint(0,2)
user = eval(input("Enter '0' for scissor, '1' for rock, '2' for paper: "))
if user == computer == 0:
    print(" Computer is Scissor, you are Scissor, It is Draw")
elif user == computer == 1:
    print("Computer is Rock, you are rock, it is Draw")
elif user == computer == 2:
    print("Computer is paper, you are paper, it is draw")
elif user == 0 and computer == 1:
    print(" The computer is rock. You are scissor.You lost")
elif user == 0 and computer== 2:
    print("The computer is paper, you are scissor, you won")
elif user == 1 and computer == 0:
    print("Computer is scissor, you are rock, you won")
elif user == 1 and computer == 2:
    print("Computer is paper, you are rock, you lost")
elif user == 2 and computer == 0:
    print("Computer is scissor, you are paper, you lost")
elif user == 2 and computer == 1:
    print("Computer is rock, you are paper, you won")
else:
    print("Wrong entry")



#SHOW CURRENT TIME
import time
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24
print(currentHour, currentMinute, currentSecond



# SORT THREE NUMBERS
def main():
    num1, num2, num3 = eval(input("Enter three integars: "))
    displaySortedNumbers(num1,num2,num3)
def displaySortedNumbers(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2,num3 = num3, num2
    if num1> num2:
        num1, num2= num2, num1
    print("The sorted numbers are ", num1, num2, num3)
main()


