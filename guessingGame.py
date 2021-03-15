import random

generator = random.randrange(1,9)

chances = 0

while chances <= 5:
    chances = chances + 1
    userInput = int(input("Enter Number"))
    if generator == userInput:
        print("You Won")
        break
    elif generator > userInput:
        print("Guess a Higher Number")
    else:
        print("Guess a Lower Number")

if not chances < 5:
    print("You Lost the Number was",generator)
