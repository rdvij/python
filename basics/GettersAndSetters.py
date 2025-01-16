class GettersAndSetters:
    def __init__(self, name, age=12):
        self.__name = name
        self.__age = age
    
    @property
    def set_name(self):
        return self.__name

    @set_name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def set_age(self, age):
        self.__age = age

    @property
    def ageAfterFiveYears(self):
        return f"Age after 5 years will be : " + str(self.__age + 5)

    def __str__(self):
        return "Name: " + self.__name + " Age: " + str(self.__age)

classObject = GettersAndSetters("John", 22)
print(classObject)
print(classObject.ageAfterFiveYears)

classObject.set_name = "Jane"
classObject.set_age = 25

print(classObject)
print(classObject.ageAfterFiveYears)