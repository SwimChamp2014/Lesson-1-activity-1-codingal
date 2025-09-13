word = input("Enter a word: ").strip()
def reversed_word():
    return word[::-1]


class Reverse:
    def __init__(self):
        print("Your word reversed is:", reversed_word())

Reverse()