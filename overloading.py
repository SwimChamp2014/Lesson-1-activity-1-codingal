class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if (self.a < other.a):
            return "ob1 is less than obj 2"
        else: 
            return "ob2 is less than obj 1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
        
obj1 = A(2)
obj2 = A(3)
print("Passed values are ", obj1.a, obj2.a)
print(obj1 < obj2)

obj3 = A(4)
obj4 = A(4)
print("Passed values are", obj3.a, obj4.a)
print(obj3 == obj4)
