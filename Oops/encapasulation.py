#Encapsulation

class Employee:
    def __init__(self,name,comp,salary):
        self.name = name  #public attribute
        self._comp = comp  
        self.__salary = salary  #private attribute
    
    def Emp_Details(self):
        print(f"EMP name {self.name}")
        print(f"Comp name {self._comp}")
        print(f"Salary: {self.__salary}")

    #get method
    def get_salary(self):
        return self.__salary
    
    #set method
    def set_salary(self,new_salary):
        self.__salary = new_salary

emp1 = Employee("patan","TCS",20000)
emp1.Emp_Details()
# print(emp1.__salary) # error trying to access private variable
print(emp1.get_salary())
emp1.set_salary(40000)
print(emp1.get_salary())

#after update 
emp1.Emp_Details()