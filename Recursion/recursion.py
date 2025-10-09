#factorial using recursion
def fact(num):
    if num<0 :
        return "Invalid"
    if num ==0 and num ==1:
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
    if num<1:
        return "Not Prime"
    if num == idx:
        return "Prime"
    if num%idx == 0:
        return "Not Prime"
    return prime(num,idx+1)
num =7
print(prime(num))

#Linear search using recursion
def linear(num,el,idx =0):
    if idx == len(num):
        return False
    if num[idx] == el:
        return True
    return linear(num,el,idx+1)

num =[12,54,45,21,56,68]
print(linear(num,4))

#reverse a num using recursion
def reverse(n,rem=0):
    if n==0:
        return rem
    return reverse(n//10,rem*10+n%10)

n= 12
print(reverse(n))



    