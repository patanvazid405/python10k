# #program to write fib seriess upto given num
# def fib(n):
#     a,b= 0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b = b,a+b
# fib(10)

# print()

# #WAP to print fib series upto or equal to that num
# def fibb(n):
#     a,b = 0,1
#     new = ""
#     for i in range(n):
#         if a<=n:
#             new+=str(a)+" "
#         a,b = b,a+b
#     return new    
# print(fibb(8)) 


# #WAP to check num in fib series or not
# def fibnocaai(n):
#     a,b = 0,1
#     while True:
#         if a == n:
#             return True
#         elif a > n:
#             print(a)
#             return False
#         a,b = b,a+b
# print(fibnocaai(100))

# #checking num in fib series or not
# def perfectSq(num):
#     result = int(num**0.5)
#     return result*result == num

# print(perfectSq(15))
        
# def fib(n):
#     val1,val2 = 5*(n**2)+4, 5*(n**2)-4
#     return perfectSq(val1) or perfectSq(val2)

# print(fib(565))

# #fib num pos in the series
# # def fibbi(n):
# #     place =1
# #     a,b = 0,1
# #     while place<n:
# #         a,b = b,a+b
# #         place+=1
# #     return a

# # print(fibbi(2))   



# def fibbi(n):
#     a,b  =0,1
#     place =1
#     while place<n:
#         a,b = b,a+b
#         place+=1
#     return a
# print(fibbi(7))    


#fibocaii upto 10 numbers
def fib(n):
    a,b = 0,1
    for i in range(n):
        print(a,end=" ")
        a,b =b,a+b
fib(10)

#fib up to the given number
def fibbi(n):
    a,b =0,1
    while a<=n:
        print(a,end=" ")
        a,b = b,a+b
fibbi(13)       

#find num in fibnocai
def infib(n):
    a,b = 0,1
    while True:
        if a==n:
            return True
        elif a>n:
            return False
        a,b = b,a+b
print(infib(11))   


#using another way using formula 5*(n**2)+4 or 5*(n**2)-4

def perfectsq(n):
    sq = n**0.5
    return sq*sq  == n
def fibfom(n):
    val1,val2 = 5*(n**2)+4 , 5*(n**2)-4
    return perfectsq(val1) or perfectsq(val2)

print(fibfom(20))

#to print a num place in fib series
def findnum(n):
    point = 1
    a,b =0,1
    while point<n:
        a,b = b,a+b
        point+=1
    return a
print(findnum(8))


