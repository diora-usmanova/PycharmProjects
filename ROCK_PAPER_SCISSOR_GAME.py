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
