#map function applies to all
#map(function,iteration)

#capitalize
fruits = ["apple","banana","grape"]
print(list(map(str.upper,fruits)))

#num str into int
nums = ['12','45','90','65']
intt = list(map(int,nums))
print(intt)

#sum of nums in a list
nums_list = [12,35,46,24,3]

def add(n):
    return sum([int(i) for i in str(n)])
rev = list(map(add,nums_list))
print(rev)

#using lambda
res = list(map(lambda n:sum([int(i) for i in str(n)]),nums_list))
print(res)


#3 finding domain in the mail
mails = ["vazidcse@gmail.com","vazidpatan@outlook.com","riyaz@yahoo.com"]

def find(dom):
    return dom.split("@")[1]

res = list(map(find,mails))
print(res)

#
nums = ['12','45','46']

# def add(n):
#     return sum([int(i) for i in n])

rev = list(map(lambda el:sum([int(i) for i in el]),nums))
print(rev)

#capital first and last
cricket = ["dhoni","kohli","raina"]

# def cap(n):
#     return n[0].upper()+n[1:-1]+n[-1].upper()

# res = list(map(cap,cricket))
rev = list(map(lambda n:n[0].upper()+n[1:-1]+n[-1].upper(),cricket))
print(rev)

#Nearest Prime to given number

def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    return False
    
def find(n):
    left,right = n-1,n+1
    while True:
        res1 = prime(left)
        res2 = prime(right)
        if res1 and res2 :
            return f"{left} {right}"
        elif res1:
            return left
        elif res2:
            return right
        left-=1
        right+=1

print(find(90))

#filter
even = [12,4,23,43,32]

# def find(n):
#     return [i for i in n if i%2==0]

print(list(filter(lambda el: el%2==0,even)))

print(list(filter(lambda x: x % 2 == 0, even)))

#to print vowel words in the list
words = ["vzd","riyaz","ayesha","rajiya","hello"]

def vowel(n):
    vowels = "aeiouAEIOU"
    return sum([1 for i in n if i in vowels])

print(list(filter(vowel ,words)))