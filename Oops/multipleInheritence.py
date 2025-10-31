class Bank:
    def __init__(self,bank_name,bank_location,balance):
        self.bank_name = bank_name
        self.bank_location = bank_location
        self.balance = balance 
    
    def bank_details(self):
        print(f"{self.bank_name} at {self.bank_location}")

class ATM:
    def __init__(self,Atm_location):
        self.Atm_location = Atm_location

    def ATM_details(self):
        print(f"ATM at location:{self.Atm_location}")

    def Withdrawal(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} was debited successfully")


 
class Customer(Bank,ATM):
    def __init__(self,acc_no,Atm_location,bank_location,bank_name,balance):
        self.acc_no = acc_no
        super().__init__(bank_name,bank_location,balance)
        ATM.__init__(self,Atm_location)

    def customer_details(self):
        print(f"available balance {self.balance} with acc_no {self.acc_no%1000}")

c1 = Customer(123456,"KPHB","Ameerpet","Canara",1000)
c1.bank_details()
c1.ATM_details()
c1.Withdrawal(100)
c1.customer_details()




    