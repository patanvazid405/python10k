nums = [10,20,30,40]
alpha = [True,False,True,True]

dict = {nums[i]: alpha[i] for i in nums(0,len(nums))}
print(dict)

nums = [10,20,30,40]
alpha = [True,False,True,True]

dict = {nums[i]: alpha[i] for i in range(0,len(nums))}
print(dict)

word = "xyz"

#sums of consecutive nums and alone nums in the word

str1 = input()
res= 0
digits=""
for i in str1:
    if i.isdigit():
        digits+=i
print(digits)        

#harshadd number
n = input("enter:")
hard_num = 0
for i in n:
    hard_num+=int(i)
if int(n)%hard_num==0:
    print("harshad num")
else:
    print("Not a harsahd num")

#automorphic number
n = int(input("enter a number:"))
digits = len(str(n))
print(digits)
sq = n**2
last_digit = sq % (10**digits)
if n == last_digit :
    print("Automorphic number")
else:
    print("not an automorphic number")

#using slicing 
n = int(input("enter a number:"))
digits = len(str(n))
sq = str(n**2)
last = sq[-1:-digits-1:-1][::-1]
if int(last)== n:
    print("automorphic number")
else:
    print("not an automorphic number")        