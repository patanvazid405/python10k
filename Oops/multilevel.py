class Company:
    def __init__(self,comp_name,base_salary):
        self.comp_name = comp_name
        self.base_salary = base_salary
    
    def company_data(self):
        print(f"company name is {self.comp_name}")

class Department(Company):
    def __init__(self,dept,comp_name,base_salary):
        self.sept = dept
        super().__init__(comp_name,base_salary)
    
    def increment(self,percent):
        res = int((self.base_salary*percent)/100)
        self.base_salary += res
        print(f"after increment salary is {self.base_salary}")

class Employee(Department):
    def __init__(self,name,id,dept,comp_name,base_salary):
        self.name = name
        self.id = id
        super().__init__(dept,comp_name,base_salary)

    def emp_details(self):
        print(f"Employee Name:{self.name} and salary is {self.base_salary}")


emp1 = Employee("vazid",121,"cse","TCS",12000)
emp1.company_data()
emp1.increment(10)
emp1.emp_details()


        