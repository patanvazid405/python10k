class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Talk(self):
        print("you can Talk..")
    def Run(self):
        print("you can Run..")

class Student(Human):
    def __init__(self,name,age,clg):
        super().__init__(name,age)
        self.clg = clg
    def welcome(self):
        print(f"Welcome {self.name} to {self.clg}")


vazid = Student("vazid",22,"MGR")
vazid.Talk()
vazid.Run()
vazid.welcome()

Rajesh = Student("Rajesh",21,"Audi")
Rajesh.welcome()
        
        
student ={
    "name" : "vazid",
    "age" : 22,
    "clg" : "MGR",
}

student["age"]="23"
print(student)

set1 = {1,34,43,2,34}
set2 = {1,24,34,2,4,5,6,53}

print(set1.union(set2))
print(set1.union(set2))
print(set1.intersection(set2))


class animal:
    def __init__(self,name):
        self.name = name
class dog(animal):
    def __init__(self,name,sound):
        super().__init__(name)    
        self.sound = sound 
    def makeSound(self):
        print(f"{self.name} makes sound {self.sound}")

dog1 = dog("Bittu","Boww Boww")  
dog1.makeSound()

# #file operations
# with open("hello.docx","a+") as f:
#     writ = f.write("welcome to python programing..")
#     print(writ)

num = int(input("number:"))

print("It is Zero" if num==0 else "even number" if num%2==0 else "odd number")

# Write a short program that prints each number from 1 to 100 on a new line. 

# For each multiple of 3, print "Fizz" instead of the number. 

# For each multiple of 5, print "Buzz" instead of the number. 

# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

for i in range (1,100):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")        

#using Terinary opeartor
new =int(input("number here:"))
print("zero" if new==0 else "FizzBuzz" if new%3==0 and new%5==0 else "Fizz" if new%3==0 else "Buzz" if new%5==0 else "dengey")


a = int(input("num1:"))
b = str(input("name:"))
c = float(input("marks:"))

print(type(a))
print(type(b))
print(type(c))

