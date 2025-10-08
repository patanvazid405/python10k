#factorial using recursion
def fact(num):
    if num>=0 and num ==1:
        return 1
    return num*fact(num-1)

num = 5
print(fact(num))

#sum of digits using recursion
def sumofdigits(num):
    if num == 0:
        return 0
    return num % 10 + sumofdigits(int(num // 10))
num = 123
print(sumofdigits(num))

#prime num
def prime(num,idx=2):
    if num==1 or num<=0:
        return False
    if num==idx:
        return "Prime"
    return prime(num,idx+1)

num =12
print(prime(num))