import random
import time

number=random.randint(1,100)

def intro():
    print("May I ask your name?")
    name = input()
    print(name, "we are going to play a game. I am thinking of a number between 1 and 100. ")
    if number % 2 == 0:
        x = "even"
    else:
        x = "odd"
    print("\nThis is an {} number".format(x))
    time.sleep(.5)
    print("Now go ahead and guess! ")

def pick():
    guessesTaken = 0
    while guessesTaken<6:
        time.sleep(.25)
        enter=(input("Guess: "))
        
        try:
            guess = int(enter)
            if guess <= 200 and guess>=1:
                guessesTaken = guessesTaken + 1
                if guessesTaken<6:
                    if guess<number:
                        print("The number you guessed is too low. ")
                    if guess>number:
                        print("The number you guessed is too high. ")
                    if guess != number:
                        time.sleep(1)
                        print("Try again!")
                    if guess == number:
                        break
        except:
            print("I don't think that " +enter+ " is a number. Sorry")
    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good job, you guessed my number in {} guesses!".format(guessesTaken))

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))       
playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    print("do you want to play again? ")
    playagain = input()              
