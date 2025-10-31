class Bank_Account:
    def __init__(self,acc_holder_name,balance):
        self.acc_holder_name = acc_holder_name
        self.balance = balance
    
    def Bank_details(self):
        print(f"Bank acc:{self.acc_holder_name} balance:{self.balance}")

class Savings_Account(Bank_Account):
    def __init__(self,intrest_rate,acc_holder_name,balance):
        self.intrest_rate = intrest_rate
        super().__init__(acc_holder_name,balance)
    
    def intrestRate(self):
        res = (self.intrest_rate*self.balance)/100
        print(f"Intrest for acc name :{self.acc_holder_name} is {res}")

class Business_Acc(Bank_Account):
    def __init__(self,intrest_rate,acc_holder_name, balance):
        super().__init__(acc_holder_name, balance)
        self.intrest_rate = intrest_rate
    

c1 = Savings_Account(10,"vazid",1000)
c1.intrestRate()
