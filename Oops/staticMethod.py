class Bank:
    def __init__(self,acc_no,bal,pin):
        self.bal = bal
        self.acc_no = acc_no
        self.pin = pin
    
    @staticmethod
    def validPIN(tempPIN):
        return len(tempPIN)==4 and tempPIN.isdigit()
    
    def deposit(self):
        amount = int(input("enter the amount:"))
        tempPIN = input("Enter PIN:")
        if Bank.validPIN(tempPIN):
            if str(self.pin) == tempPIN:
                self.bal+=amount
                print(f"{amount} deposited successfully in acc {self.acc_no%1000}")
            else:
                print("Invalid PIN")
        else:
            print("PIN not 4digit and not Number")
        
    def withdraw(self):
        amount = int(input('Enter the amount:'))
        temp_PIN = input("Enter the pin:")
        if Bank.validPIN(temp_PIN):
            if str(self.pin) == temp_PIN:
                if amount<= self.bal:
                    self.bal-=amount
                    print(f"{amount} debited successfully")
                    print(f"Remaining Bal {self.bal}")
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid PIN")
        else:
            print("Not a 4 digit PIN")


b1 = Bank(1234567,2300,1812)
b1.deposit()
b2 = Bank(1335,1000,1812)
b2.withdraw()