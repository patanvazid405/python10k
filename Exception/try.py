# def eligible(percent):
#     if percent>75:
#         print("passed")
#     else:
#         raise ValueError("Not Eligible")

# try:
#     eligible(8)
# except ValueError as msg:
#     print(msg)

# #assert for strong num
# import math
# num = int(input())
# temp = num
# res = 0
# while temp!=0:
#     rem = temp%10
#     res += math.factorial(rem)
#     temp = temp//10
# assert num == res
# print("Strong Num")

# #using assert in
# def validate(num):
#     for i in num:
#         assert (i<50),"failed"
#         print("passed")
# list1 = [12,45,35,76,98,24]

# try:
#     validate(list1)
# except AssertionError as msg:
#     print(msg)

#
def withdraw(bal,amount):
    if bal>0:
        if amount<=bal:
            print(f"Amount:{amount} Withdrawal Successfully")
        else:
            raise ValueError("Insufficient Balance")
        
amount=int(input("Enter the amount:"))
try:
    withdraw(1200,amount)
except ValueError as msg:
    print(msg)

#marks 
def get_marks(marks):
    for i in marks:
        if i<0: 
            raise ValueError ("Invalid Marks")
        else:
            print ("valid marks")
        
myMarks = [45,0,35,78]
try:
    get_marks(myMarks)
except ValueError as msg:
    print(msg)

