#function
def greet(name):
    msg = "welcome to 10k coders"+ name
    return msg
print(greet("vazid"))

#sum of two nums 
def summ(n1,n2):
    return n1+n2
print(summ(12,5))

#division of two numbers
def div(n1,n2):
    if n1==0  and n2 ==0:
        return "Enter valid number"
    return n1//n2
print(div(12,5))

#to get key in dict using func
# def dic(key):
#     return key['a']
# res = dic({a:"A",b:"B"})
# print(res)

#palindrome using func
def Palindrome(num):
    if num < 1 :
        return False
    return num == int(str(num)[::-1])

print(Palindrome(281))


#Practice work
# 1) Write a function and find factorial of a number, return the factorial value 

def fact(num):
    factt = 1
    if num<0:
        return "Invalid Num"
    for i in range(1,num+1):
        factt*=i
    return factt

print("factorial is :",fact(-1)) 

# 2) Write a function and find smallest number in the list, return the smallest element

def small(num):
    smallest = min(num)
    return smallest

print("Smallest Number is :",small([12,79,41]))

#types of function parameters
# 1. Default
def hello(name,clg="MGR"):
    return name-" Welcome to " ,clg 
print(hello("vazid"))

# 2. positional arguments
def hi(name,clg,dept):
   return name+clg+dept
print(hi(clg="mgr",name = "vazid",dept ="cse"))

# 3. *args
def bye(*args):
    return args

print(bye("vazid",22,"patan"))

#4 . **keyargs
# def keyargs(**keyargs):
#     return keyargs
# print(keyargs("heelo","hi","welcome"))


#fibonacci series upto 
def fibonacci(num):
    a,b = 0,1
    res = " "
    for i in range(num):
        res+=str(a)+" "
        a,b = b,a+b
    return res    

print(fibonacci(5))
        
#fibonacci series upto num
def fib(n):
    res = ""
    a,b = 0,1
    for i in range(n):
        if a<=n:
            res+= str(a)+" "
            a,b = b,a+b
    return res        
print(fib(13)) 


            
