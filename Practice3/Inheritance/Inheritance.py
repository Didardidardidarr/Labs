class Class:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printall(self):
        print(f"{self.name} is my name and {self.age} is my age")
p1 = Class("Noob Saibot",999)
p1.printall()



class Class:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printall(self):
        print(f"{self.name} is my name and {self.age} is my age")
class Student(Class):
    pass
p1 = Student("Noob Saibot",999)
p1.printall()



class Class:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printall(self):
        print(f"{self.name} is my name and my age is {self.age}")
class Student(Class):
    def __init__(self,name,age,eye_colour):
        super().__init__(name,age)
        self.eye_colour = eye_colour
    def printname(self):
        print(f"My name is {self.name} and my age is {self.age}.Also my eye colour is {self.eye_colour}")   
p1 = Student("Robert", 19, "blue")
p1.printname()                     