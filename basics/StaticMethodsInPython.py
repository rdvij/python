class StaticFunction:
    @staticmethod
    def static_method():
        print("This is a static method")
    
    @classmethod
    def class_method(cls):
        print("This is a class method")

    def normal_method(self):
        print("This is a normal method")

StaticFunction.static_method()
StaticFunction.class_method()

sf = StaticFunction()
sf.normal_method()

# Using Class methods for factory methods
import datetime as datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, datetime.datetime.now().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18
    
person1 = Person('Raj', 21)
person2 = Person.fromBirthYear('Jane', 1990)

print(str(person1.age) + " & " + person1.name)
print(str(person2.age) + " & " + person2.name)