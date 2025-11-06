class Bank:
    def __init__(self,name,acc_no):
        self.name = name
        self.acc_no = acc_no
    
    def withdrawal(self):
        print("Withdraw")
    
#monkey patching 
def withdraw(self,amount):
    print(f"{amount} was debited successfully")


# Bank.withdrawal = withdraw   #for whole class method

c1  = Bank("vazid",123)
c1.withdrawal()
c2 = Bank("patan",1236)
Bank.withdrawal = withdraw.__get__(c2,Bank)  #only for particular object patching

c2.withdrawal(1000)

