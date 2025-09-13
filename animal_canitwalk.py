from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run.")

class Snake(Animal):
    def move(self):
        print("I can slither around.")
        
class Dog(Animal):
    def move(self):
        print("I can crawl around.")

dog_object = Dog()
human_object = Human()
snake_object = Snake()

dog_object.move()
human_object.move()
snake_object.move()