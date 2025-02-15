import random

number = int(random.randint(1, 9))

print("Welcome to this game in which you have to choose the correct number.\n If you wish to win you have to choose the correct number between 1 and 9")

guess = int(input("Enter the number that you think the computer has guessed: "))

num = 0

while guess != number:
    guess = int(input("Try again: "))
    num = num + 1
    if num == 2:
        print("You have lost the game")
        break

    


if guess == number:
    print("You have won")