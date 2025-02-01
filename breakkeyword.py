word = input("Enter a word of your choice in capital letters: ")
character = input("What letter do you want to find in your word choice(please write in capitals)? ")

for i in word:
    if i == character:
        print("I have found the letter", character, "in your", word)
        break
    else:
        print("The letter", i, "is not", character)
