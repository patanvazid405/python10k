# 1.default parameters
def addition(n1,n2,n3=0):
    return n1+n2+n3
print(addition(1,2))
print(addition(1,2,3))

#2.positional arguments

def details(name,age,sal):
    text = f"Name:{name}, Age:{age} ,Sal:{sal}"
    return text
print(details("vazid",23400,22)) #not based on pos we can give were we want not an order

# 3. keyword arguments
def det(name,age,sal):
    text = f"Name:{name}, Age:{age} ,Sal:{sal}"
    return text
print(det(name="vazid",age=22,sal=21000))

# 4. arbitrary parameters *
    # *args -> multiple arguments
    # **args  -> multiple args in key and value pair

def add(*args):
    arguments = len(args)
    if arguments == 0:
        return "No values"
    return f"Sum of {arguments} is {sum(args)}"
print(add(10,34,12))

#2
def price(*args):
    if len(args) ==3:
        return f"Price is {args[1]*args[2]}"
    elif len(args)==2:
         return "Not a valid price given"
    else:
        return "Enter the values"
print(price("pen",3,5))    
print(price("pen",3))    
print(price())    

# **kargs it will make into key and value pairs

def karg(**kargs):
    return kargs

print(karg(name="vazid",age=20,clg="MGR"))


#
name = "vazid"
def greet():
    global name
    print("Hello",name)

greet()

#local and global variables and non local variable\
x = 12
def num():
    x = 55
    print(x)

num()

#accessing global in func
x = 12
def new():
    global x
    x = x+12
    print(x)
new()   

#WAP to show the non local 
x = 123
def first():
    x = 12
    print("Outer func 1")
    print(x)
    def second():
        nonlocal x
        x = x+12
        print("inner function")
        print(x)
    second()
    

first()








