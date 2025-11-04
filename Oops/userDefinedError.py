class BalError(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)  # You don’t need self,msg — only msg

class Bank:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal
    
    def withdrawal(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f"Withdrawal successful! Remaining balance: {self.bal}")
        else:
            raise BalError("Insufficient funds")

try:
    c1 = Bank("vazz", 1000)
    c1.withdrawal(2000)
except BalError as msg:
    print(msg)


#example2

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
