#1 Sum of Digits in a Number (Without Using Methods) 
n = 12345
temp =n
sum = 0
for i in str(n):
    rem = temp%10
    sum+=rem
    temp= temp//10
    
print(sum)

#2 
ex = "programming"
uni =""
dup = ""

for i in ex:
    if i not in dup:
        dup+=i
    else:
        uni+=i  
print(uni)

#3
inp = [2,3,2,5,6,5]
unq = []
dup =[]
for i in inp:
    if i in unq:
        unq.append(i)
    else:
        dup.append(i)

    
print(dup)

