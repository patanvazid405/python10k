#1
#Reverse a Number without using Slice Method
n = 1234
temp = n
res = 0
for i in range(len(str(n))):
    rem = temp%10
    res = res*10+rem
    temp=temp//10
print(res)

#2
#print fibonacci series upto the given number
def fib(n):
    a,b = 0,1
    for i in range(0,n):
        if a<=n:
            print(a,end=" ")
        a,b = b,a+b

fib(105)

print()
#3
#perfect Number
def perfect(n):
    summ = 0
    for i in range(1,n):
        if n%i==0:
            summ+=i
    if int(summ) == n:
        print("perfect Square")
    else:
        print("Not a Perfect Square")

perfect(10)

