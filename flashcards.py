class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + '('+self.meaning+')'

flash = []
print("Welcome to a flashcard application! ")

while(True):
    word = input("Enter the name you want to add to your collection of flashcards: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 if you want to  add another flashcard, otherwise enter 1: "))

    if (option):
        break

print("\nYour flashcards: ")
for i in flash:
    print(">", i)