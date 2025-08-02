class Dog:
    species = "dog"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

kashi = Dog("Kashi", 4, "Golden Doodle")
dobby = Dog("Dobby", 5, "Golden Retriever")

print("Kashi is  a {}, and his breed is a {}".format(kashi.species, kashi.breed))
print("Dobby is a {}, and his breed is a {}".format(dobby.species, dobby.breed))

print("{} is {} years old".format(kashi.name, kashi.age))
print("{} is {} years old".format(dobby.name, dobby.age))
