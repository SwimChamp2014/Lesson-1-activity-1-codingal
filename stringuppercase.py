class IOString():

    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter String : ")

    def print_String(self):
        print("result is :", self.str1.upper())

    # Creates object
str1 = IOString()

str1.get_String()
str1.print_String()