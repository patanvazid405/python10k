#inheritance 
#single inheritance
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} he can speak")

class student(person):
    def __init__(self,course,fee):
        self.course = course
        self.fee = fee
        super().__init__("vazid",22)
    def practice(self):
        print(f"{self.name} he can practice {self.course}")
        super().speak()

p1 = person("vazid",22)
p1.speak()

s1 = student("python full stack",30)
print(s1.course)

s1.practice()


class company:
    comp = "TCS"
    def __init__(self):
        self.projects = ["NLP","AWS","Python"]
    
    def show_projects(self):
        print(f"available projects {self.projects}")


class employee(company):
    def __init__(self,name,id):
        self.name = name
        self.id = id
        super().__init__() #calling parent class constructor
        # print(self.projects)

emp1 = employee("rajesh",123)
emp1.show_projects()
print(emp1.comp)






