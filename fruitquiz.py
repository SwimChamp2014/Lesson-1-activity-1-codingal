import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple': 'red', 'orange': 'orange', 'watermelon' : 'green', 'banana' : 'yellow'}
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            user_answer = input(print("What is the color of {}".format(fruit)))
            if (user_answer.lower() == color):
                print("You have thought of the correct answer. ")
            else:
                print("You have thought of the wrong answer. ")
            option = int(input("Enter 0 if you want to play again, otherwise enter 1: "))
            if(option):
                break
print("Welcome to fruit quiz! ")
fruit_quiz = FruitQuiz()
fruit_quiz.quiz()
            