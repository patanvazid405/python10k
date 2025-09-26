strs = ["apple","banana","grape"]

res = list(map(str.upper,strs))
print(res)

#2
list1 = ['12','45','76']
def summ(n):
    return sum([int(i) for i in n ])
print(list(map(summ,list1)))

#filter
names = ["kohli", "dhoni", "raina", "sachin"]

def vowel(n):
    vowels = "aeiouAEIOU"
    return any(ch in vowels for ch in n)

x = list(filter(vowel, names))
print(x)


#reduce
from functools import reduce
list1 = [45,234]
print(reduce(lambda x,y: x+y ,list1))

nums =[120,31,23]
print(reduce(lambda x,y : x+y,nums))

#using filter nd reduce

from functools import reduce

heros = ["Pawan", "mahesh", "prabhas", "Vijay"]

# filter names starting with uppercase letter
y = list(filter(lambda v: v[0].isupper(), heros))

# join them with spaces
x = reduce(lambda a, b: a + " " + b, y)

print(x)

even = [12,4,23,43,32]

# def find(n):
#     return [i for i in n if i%2==0]

print(list(filter(lambda el: el%2==0,even)))

print(list(filter(lambda x: x % 2 == 0, even)))

