

# j = 0
# while j<=10:
#     print(j)
#     j+=1

# inp = int(input("Enter a number: "))

# k = 0
# while k <= inp:
#     print(k)
#     k += 1

# inp = int(input("Enter a number: "))

# k = 0
# while k <= inp:
#     print(k)
#     k += 1



# k = 0
# while k <= inp:
#     print(k)
#     k += 1


#fact 
user_inp = int(input("Enter a Number "))
fat =1 
for i in range(1,user_inp+1):
    fat*=i
print(fat)    

#sum
user_inp = int(input("Enter the number"))
sum = 0
for i in range(1,user_inp+1):
    sum+=i
print(sum)    

user = int(input("Number here:"))
i = 1
sum = 0
while i<=user:
    sum+=i
    i+=1
print(sum)    

user = int(input("Number here: "))
i = 1
sum = 0
while i <= user:
    sum += i
    i += 1
print("Sum is:", sum)


#fact

inp = int(input("Enter the Number:"))
fact =1
i =1
while i<=inp:
    fact*=i
    i+=1
print(fact)

#fact using while loop
new = int(input("Number Here:"))
factt =1
for i in range(1,new+1):
    factt*=i
print(factt)    

#sum
h = int (input("Enter the NUm:"))
sum = 0
i = 1
while i<=h:
    sum+=i
    i+=1
print(sum) 


n = 10
i = 1
while i<=n:
    print(i)
    i+=1  


m =10
n = 20
for i in range(m,n+1):
      print(i)

# m =3
# n =7
# while m<n:
#     print(m)
#     m+=1

a =23.856
print(round(a,2))

#table using for loop
intt = int(input("Enter the NUmber:"))

# for i in range(1,11):
#     print(f"{intt} X {i} =",intt*i)

i = 1
while i<=10:
    print(f"{intt} X {i} =",intt*i)   
    i+=1
    
#factorail
intt = int(input("Enter the NUmber:"))
fact = 1
for i in range(1,intt+1):
    fact*=i

print(fact)  

#fact using while
inp = int(input("Number:"))
i = 1
fact = 1
while i<=inp:
    fact*=i
    i+=1
print(fact) 


inp = int(input("Enter the Number:"))
fact =1
i =1
while i<=inp:
    fact*=i
    i+=1
print(fact)

#sum
new = int(input("Sum:"))  
sum =0
for i in range(0,new+1):
    sum+=i
print(sum)    

#sum using while 

new = int(input("Sum:"))  
sum = 0
i = 0
while i<=new:
    sum+=i
    i+=1
print(sum)    

#oops

class car:
    def __init__(self,model,brand,year):
        self.model = model
        self.brand = brand
        self.year  = year

    def carDetails(self):
        print("car model:",self.model)    
        print("car Brand:",self.brand)    
        print("car Year:",self.year)    

    def start(self):
        print(f"{self.model} is Starting Now...")

car1 = car("Nexon","TATA",2023)
car2 = car("Z6","BMW",2024)

car1.carDetails()
car1.start()

car2.carDetails()
car2.start()

class bike(car):
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model =  model
        self.year = year
       
    def welcome(self):
        print(f"Welcome to {self.brand} ") 

hero = bike("Hero","HF Deluxe",2010)
hero.carDetails()
hero.start() 

#human class  and person
class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Details(self):
        print(f"Welcome {self.name} Your Age is {self.age}")  
    def walk(self):
        print(self.name,"Started walking..")
    def rest(self):
        print(self.name,"take rest !")

class student(human):
    def __init__(self,college,marks,name,age):
        self.college = college
        self.marks = marks
        super().__init__(age,name)
    def marks(self):
        print("You marks are:",self.marks)

class Employee(human):
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        super().__init__(age)

    def emp_info(self):
        print("hello",self.name," Your Id is:",self.id)

vazid = student("MGR",89,"Vazid",22)
niteesh = student("Vits",80,"Niteesh",21)

vazid.Details()
niteesh.walk()
# print(vazid.age(22))





for i in range(1,5):
    print("*"*i)

ran = int(input("num:"))

# i = 1
# while i<=range:
#     print("*"*(i-1))
#     i+=1

for i in range(0,ran+1):
    print("*"*i)

put = int(input("Hello Num:"))

# for i in range(0,put+1):
#     print("*"*(put-i))
i = 0
while i<=20:
    print("*"*(20-i))
    i+=1 
for i in range(0,20):
    print("*"*i)    


my_list = ["vazid",22,8.56,"Mudivarthi Palem"]
print(my_list[0])
print(my_list[-1:])
print(my_list[:4])
print(my_list[2])
print(my_list[0]) 


my_list.append("MGR University")
my_list.remove("Mudivarthi Palem")
print(my_list)

def hello(name):
    print("Hello",name)

hello("vazid")

my_list =["vazid",22,80,["cse","MGR","F"]]

print(my_list[3][2:])





# print(car1.model)
# print(car2.model)


come =  input("Enter name and age:")

a,b = come.split(",")
print(f"Name is {a} age is {b}")

#tuple
marks = (12, 34, 12, 12, 11)
print(marks) 
print(marks.count(12))
print(marks.index(34))

#sets
name1 = {"vazid","niteesh","rajesh"}
name2 = {"vazid","nikhil","rajesh","harsha"}

print(name1.add("satish"))
print(name1.add("rakesh"))
print(name1.remove("rakesh"))

print(name1.union(name2))
print(name2.intersection(name1))

#dict
person = {
    "nme":"vazid",
    "age": 22,
    "clg":"MGR",
    "marks" : 8.90
}
print(person["nme"])
person["age"]=12
print(person["age"])

#amount
class Acc_Details():
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def credit(self,cred_amount,):
        self.cred_amount = cred_amount
        print(cred_amount)

    def show_bal(self):
        print(credits())

acc1 = Acc_Details("vazid",121,1200)
acc1.credit(2000)
print(acc1.acc_no)



import random

# for i in range(1):
user_inp = int(input("Enter Number Here:"))
rand = random.randint(1,5)
if rand == user_inp:
    print("you gussed right bro")
else:
     print("Wrong mawa")   

import matplotlib.pyplot as pf

x =[2021,2022,2023,2024]
y =[80,82,79,86]

pf.plot(x,y)
# pf.plot(y)
pf.show(x,y)

import turtle

pt = turtle.Turtle()

for i in range(6):
    pt.forward(200)
    pt.left(90)
    pt.right(30)
turtle.done() 


import  turtle
hlo = turtle.Turtle()

for i in range(15):
    hlo.forward(20)
    hlo.right(50)
    hlo.backward(50)
    hlo.left(20)
turtle.done()

import turtle
lop = turtle.Turtle()

for i in range(1,1000):
    lop.forward(70)
    lop.right(30)
    lop.left(20)
    lop.backward(70)
turtle.done()    


#oops

class Acc:
    def __init__(self,name,id,bal):
        self.name = name
        self.id = id
        self.bal =bal    
    def credit(self):
        cred = int(input("enter amount:"))
        cred = cred+self.bal
        print(cred)
    def debit(self):
        debt = int(input("enter amount:"))
        debt = debt-self.bal
        print(debt)
 



acc1 = Acc("Vazid",112,2000)
acc2 = Acc("Niteesh",103,1000)

acc1.credit()
acc2.debit()



name = "rajesh"
print("hello",name)

def Myname(name):
    print("Hello",name)

Myname("vazid")
Myname("Putta Rajesh")


import random

num = random.randint(1,5)

for i in range(1,4):
    user_otp = int(input("ENter OTP:"))

    if user_otp == num :
        print("You can login")
    else:
        print("wrong OTP")    

    print("OTP:",num)


import turtle

hi = turtle.Turtle()

for i in range(1,20):
    hi.forward(20)
    hi.left(30)
    hi.back(20)
    hi.forward(30)
turtle.done()    

#patterns
i = 0
while i<=10:
    j =0
    while j<=10-i:
        print('*',end="")
        j+=1
    print()
    i+=1    


for i in range(1,10):
    print(i)

Emp1 = [101,"vazid",22,"Mudivarthi Palem"]
Emp2 = list(input("Enter Emp Details:".split(",")))
print(f"Employee details {Emp1} and type is {type(Emp1)}")
print(f"Employee info {Emp2} and type is {type(Emp2)}")










