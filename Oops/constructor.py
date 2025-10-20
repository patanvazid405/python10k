class Bank:
    pin = 1812
    def __init__(self,name,acc,bal):
        self.name = name
        self.acc = acc
        self.bal = bal

    def balance(self):
        print(f"Available Bal in acc {self.acc%10000} is {self.bal} ")
    
    def deposit(self,amount):
        am = self.bal+amount
        print(f"{amount} Deposited Successfully..")
        print(f"Available Balance is {am} ")
    
    def withdrawal(self,amount):
        inp = int(input("Enter PIN:"))
        if inp == self.pin:
            if self.bal >= amount:
                av = self.bal - amount
                print(f"{amount} amount debited successfully")
                print(f"{av} is balance")
            else:
                print("Insufficient Balance")
        else:
            print("Wrong Pin")


c1 = Bank("vazid",9390715405,2500)
c1.balance()
c1.deposit(1200)
c1.withdrawal(500)