word = input("Enter a word: ")

character = input("Please enter a Character in the word: ")

i = 0
count = 0

while (i < len(word)):

    if (word[i] == character):
        count = count + 1
    i = i + 1

print("The total number of times", character, "has occured is = ", count)