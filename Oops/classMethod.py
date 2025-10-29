class Bank:
    intrest_rate = 5.0
    ifsc_code = "CNRB13482"

    def __init__(self,acc_no,bal):
        self.acc_no = acc_no
        self.bal = bal
    
    @classmethod   #using classmethod we can change directly change the class instance 
    def update_intrest(cls):
        cls.intrest_rate = 4.5

    @classmethod
    def update_ifsc(cls):
        cls.ifsc_code = "SBIN1324"

c1 = Bank(12345,2000)
print(c1.__dict__)
Bank.update_intrest() #updating class variable
Bank.update_ifsc()
print(c1.ifsc_code) #after update changed
print(c1.intrest_rate)
c2 = Bank(1245,6790)
print(c2.ifsc_code)


class Emp:
    company = "TCS"
    def __init__(self,name):
        self.name = name
        # self.company = company
    
    @classmethod
    def update_company(cls):
        cls.company = "Deloitte"

emp2 = Emp("vazid") 
print(emp2.__dict__)
Emp.update_company()
print(emp2.company)
