from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside an Absclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

test_object =  test_class()
test_object.task()
test_object.print(100)


        
