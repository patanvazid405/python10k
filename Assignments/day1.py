#1
n = int(input("Enter the Number:"))
for i in range(2,int(n**0.5)+1):
    if  n%2==0:
        print(" Not a Prime")
    else:
        print("Prime")

#2
n# n = 7
def factorial(n):
    fact = 1
    exp = ""
    for i in range(1,n+1):
        if i != 1:
            exp+=" X"
        exp+=str(i)
        fact*=i
    return fact

print(factorial(5))

#3
def fibonacci(n):
    a,b = 0,1
    for i in range(0,n):
        if a<=n:
            print(a,end=" ")
            a,b = b,a+b
        elif a>n:
            break
        
fibonacci(50)


def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
    
def hello():
    print("hello")
@my_decorator
def hello():
    print("hello")