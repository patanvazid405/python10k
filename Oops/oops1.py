class dog:
    def details(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"🐶 {self.name} is barking")
    def eat(self):
        print(f"🐶 {self.name} is eating")

dog1 = dog()
dog1.details("bittu",2)
dog1.bark()
dog1.eat()

#class 
class car:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        print(f"{self.name} model is {self.model} and model is{self.year}")
    def start(self):
        print("car is starting...")
    def stop(self):
        print("car is stopped...")

car1 = car("Tata","Curv v",2024)
car1.start()
car1.stop()

#Instance variables and class variable -> is a variable in a class
#inside the class and inside the method

class Employee:
    company_name = "TCS"

    def set_details(self,name,city):
        self.name =name 
        self.city = city
    def ShowDetails(self):
        print(f"Name:{self.name} city:{self.city}")
    def changeCity(self,city):
        self.city = city

e1 = Employee()
e2 = Employee()
e1.set_details("vazid","Nellore")
e1.ShowDetails()
print(Employee.company_name) # for all employees having TCS as default company
print(e1.__dict__) #shows instances of object
e2.set_details("rahil","kothur")
e2.company_name="Wipro"
print(e2.__dict__)
e2.ShowDetails()

#deleting class instance and methods

class Person:
    clg = 'MGR'
    def intro(self,name,age):
        self.age = age
        self.name = name
    def hello(self):
        print(f"hi {self.name} happy diwali")

p1 = Person()
p1.intro("vazid",22)
p1.hello()
p2 = Person()

#deleting an instance variable
del p1.age #deleting an instance variable
print(p1.__dict__)
del p2 #deleting an object
# print(p2.__dict__)

del Person #deleting an class
print(Person)

print(Person.clg)
del Person.clg #Deleting an class variable

p1.hello = None #del a method to that particular object
print(p1.hello())


