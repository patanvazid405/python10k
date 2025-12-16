#practice

from turtle import right


a = 5
a+=1
print(a)

#ternary 
num = 10
res =  "positive" if num>1 else "negative"
print(res)

#conditional statements
# if,elif,else

#for loop
for i in range(5):
    print(i)

list1 = [12,34,13,34]

for i in range(len(list1)):
    print(list1[i])

#while loop
i = 1
while i<=5:
    print(i)
    i+=1

num = 5
for i in range(1,num+1):
    print(i)

for i in range(-num,0):
    print(i)   #minus values -5,-4,-3,....

for j in range(-5,6):
    print(j,end=" ")

print()
#factorial
n = 7
fact =1
for i in range(1,n+1):
    fact*=i
print("factorial:",fact)

#using while loop factorial
fact = 1
n = 7
i=1
while i<=n:
    fact*=i
    i+=1
print("fact",fact)


#sum of num
sum=0
for i in range(1,n+1):
    sum+=i
print("sum",sum)

#using while loop sum of numbers
n =7
i = 1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)

#[pattern]
n = 6
for i in range(1,n+1):
    print(n*"*")

#half triangle
print(" half triangle")
for i in range(1,n+1):
    print("*"*i)

#half triangle rev
for i in range(n,0,-1):
    print("*"*i)

#full triangle
for i in range(1,n+1):
    spc = " "*(n-i)
    strr = " *"*i
    print(spc+strr)

#nums pattern
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# rev num pattern
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

#read the num until th given number is even

inp = int(input("enter thr num:"))
list1 = []

if inp%2==0:
    list1.append(inp)

while inp%2 != 0:
    inp = int(input("Enter Again!"))
    if inp%2 ==0:
        list1.append(inp)
        print("even number added ")
        break

#prime or not 
n = int(input())
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not prime Number !")
            break
        
        else:
            print("Prime Number")

#lcm and gcd

def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a
print(gcd(12,6))

#lcm 
def lcm (a,b):
    print(a*b // gcd(a,b))

lcm(12,5)

# list comprehension

list1 = [ int(i**2) for i in range(1,11) if i%2==0]
print(list1)

string = "vwdyv wdhvu uvc"
s1 = string.split(" ")
print(s1)

#duplicates
n = map(int,input().split())

uniq,dup="",""

for i in n:
    if str(i) not in uniq:
        uniq+=str(i)+" "
    else:
        dup+=str(i)+" "

print(uniq)
print(dup)


#max,sec_max min,sec_min
nums = list(map(int,input().split()))

max_num = sec_max = nums[0]
min_num = sec_min = nums[0]

for i in nums[1:]:
    if i>max_num:
        sec_max = max_num
        max_num = i
    elif i>sec_max and i<max_num:
        sec_max = i
    
    if i<min_num:
        sec_min = min_num
        min_num = i

print(max_num,sec_max)
print(min_num,sec_min)


#count words
word = "hello welcome to hyderabad"
new = dict()
for i in word:
    if i == " ":
        continue
    print(i,word.count(i))


#largest word in the string

new_word = word.split()
max_len_word = 0
max_word = ""
for i in new_word:
    
    if len(i)> max_len_word:
        max_word = i
    
    elif len(i) == max_len_word:
        max_word += " "+i

print(max_word)


#dict
d1 = {
    "name" :"vazid",
    "age"  : 23,
    "city" : "NLR"
}
for i in d1:
    print(i,d1[i])
#keys
for i in d1:
    print(i)
print(d1.keys())
#values
for i in d1:
    print(d1[i])

#
print(d1["age"])
print(d1.get("city"))

#methods in dict
print(d1.items())
print(d1.keys())
print(d1.values())

#update
d1.update({"marks":90,"clg":"MGR"})
print(d1)

capitals = {
    "India" : "Delhi",
    "UK" : "London",
    "USA" : "Wc dc"
}

res = {}
for i in capitals:
    country = i
    capital = capitals[i]
    res[capital] = country

print(res)

#palindrome

num = int(input("enter a num:"))
if num>0:
    rev = int(str(num)[::-1])

print("palindrome" if rev==num else "Not a palindrome")


#nearest  prime

def is_prime(n):
    if n>1:
        for i in range (2,int(n**0.5)+1):
            if n%i ==0 :
                return False
        return True
    return False
# print(is_prime(10))

n = 16
left = n-1
rightt = n+1

while True:
    res1 = is_prime(left)
    res2 = is_prime(rightt)

    if res1 and res2:
        print(left,rightt)
        break
    elif res1:
        print(left)
        break
    elif res2:
        print(rightt)
        break
    left-=1
    rightt+=1

#map func

strs = ["apple","banana"]
print(list(map(str.upper,strs)))

nums = ['10','20','30']

def add(el):
    return sum([int(i) for i in el])
res = list(map(add,nums))

rep = list(map(lambda el: sum([ int(i) for i in el]),nums))
print(rep)
print(res)



x = lambda a,b: a+b
print(x(12,3))


#reverse a num witihout method

num =134
temp =num
rev =0

while temp !=0:
    rem = temp%10
    rev = rev*10+rem
    temp= temp//10
# assert(temp==num)
print("strong num")


#file read

with open("hello.txt","w+") as file:
    data = file.read()
    file.close()







