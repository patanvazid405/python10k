#day4
#local # global # nonLocal

#global
x = 100
def outer():
    global x
    x +=10
    print(x)
outer()
print(x)

#local
y =10
def innner():
    y =15
    print(y)
innner()
print(y)

#Non local used in Nested function
x  = 10
def outer():
    x = 15
    def inner():
        nonlocal x
        x+=1
        print("inner",x)

print(outer())
# inner()


#2
vowels = "aeiouAEIOU"

word  = "education"
for i in word:
    if i not in vowels:
        print(i,end=" ")

print()

#3
n  = "Hello@123"
alpha = 0
digi = 0
spec = 0
for i in n:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digi+=1
    else:
        spec+=1
print("Alphabets",alpha)
print("Numbers",digi)
print("Special Char",spec)