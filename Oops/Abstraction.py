#Abstraction ->hiding some methods 

from abc import ABC,abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("vehicle is started")
    
    def stop(self):
        print("Vehicle is stopped")
    
c1= Car()
c1.start()
c1.stop()


from abc import ABC,abstractmethod

class Amount(ABC):

    @abstractmethod
    def cal_intrest(self):
        pass

    @abstractmethod
    def withdrwal(self):
        pass

class Saving_Acc(Amount):
    def __init__(self,bal):
        self.bal =bal
    
    def cal_intrest(self,time):
        print(f"available instrest amount {(self.bal*time*2.5)}")
    
    def withdrwal(self,amount):
        if amount <=self.bal:
            self.bal -= amount
            print("Withdraw done")
        else:
            print("Insufficient Balance")

c1 = Saving_Acc(2000)
c1.cal_intrest(10)
c1.withdrwal(1000)


