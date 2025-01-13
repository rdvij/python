class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, team, *developers):
        super().__init__(name, salary)
        self.team = team
        self.developers = developers
        self.__secretName = team + "_" + name

    def display(self):
        super().display()
        print("Secret Name: ", self.__secretName)

        print("Team: ", self.team)
        print("Developers: ")
        print("Senior Developers: ", len(list(filter(lambda x: x.type() == "JuniorDeveloper", self.developers))))
        print("Junior Developers: ", len(list(filter(lambda x: x.type() == "SeniorDeveloper", self.developers))))

class Developer(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.project = project

    def display(self):
        super().display()
        print("Project: ", self.project)

    def type(self):
        return type(self).__name__
    
class JuniorDeveloper(Developer):
    def __init__(self, name, salary, project, experience):
        super().__init__(name, salary, project)
        self.experience = experience

    def display(self):
        super().display()
        print("Experience: ", self.experience)

class SeniorDeveloper(Developer):
    def __init__(self, name, salary, project, experience):
        super().__init__(name, salary, project)
        self.experience = experience

    def display(self):
        super().display()
        print("Experience: ", self.experience)

Developer1 = JuniorDeveloper("Raj", 50000, "MFX", 5)
Developer2 = SeniorDeveloper("Jane", 100000, "MFX", 9)

#print(type(Developer1))
#print(type(Developer2))
#print(Developer1.type())

Manager1 = Manager("John", 90000, "MFX", Developer1, Developer2)

#print(Manager1.__secretName)
Manager1.__secretName = "modified"
print("*** " + Manager1.__secretName + " ***")
Manager1.display()