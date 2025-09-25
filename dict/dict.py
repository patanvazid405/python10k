d1 = {
    "name" : "vazid",
    "nootes" : []
}
notes = d1["nootes"]
if notes:
    avg =  sum(notes)//len(notes)
    d1["nootes"] = avg
else:
    d1["nootes"] = 0

print(d1) 

#sorted words palindrome
n = input("enter words:").split()
n.sort()
new=[]
max_palin,max_len = "",0
for word in n:
    if word== word[::-1]:
        new.append(word)
    else:
        print("not a palindrome")  
    length = len(word)
    if length>max_len:
        max_len = length
        max_palin = word    

print(new) 
print(max_len)
print(max_palin)       

# #factorail 
# n = input("enter:")
# summ = 0
# temp = n
# while n>0 :
#     rem = n%10
#     fact=1
#     for i in range(1,rem+1):
#         fact*=i
#         summ+=fact
#     print(fact)
#     temp =temp//10
# print(summ) 


#make alpha and digit separate in dict
n = input("enter here:").split()
dictt = dict()
for i in n:
    alpha =""
    digit = ""
    for j in i:
        if j.isalpha():
            alpha+=j
        if j.isdigit():
            digit+=j
    dictt[alpha] = digit
    
print(dictt)        
        
#cal budget of three persons in the three dicts all in one list 
persons = [{"name":"vazid", "age":22,"budget" : 2399},
           {"name":"niteesh", "age":21,"budget" : 4569},
           {"name":"rajesh", "age":22,"budget" : 2569},]  
total_budget = 0
for i in persons:
    total_budget+=i["budget"]
print(total_budget)       

#add budget in another way taking input from the user
n = int(input("enter:"))
temp = []
for i in range(n):
    details = input("enter details:").split()
    dictt = dict()
    temp["name"],temp["age"],temp["budget"] = details[0],details[1],details[-1]
    print(dictt)

n = int(input("enter:"))
temp = []
add = 0
for i in range(n):
    details = input("enter details:").split()
    dictt = dict()
    dictt["name"],dictt["age"],dictt["budget"] = details[0],details[1],details[-1]
    temp.append(dictt)
    
for i  in temp:
    add+=int(i["budget"])
print(add) 


#avg of notes

d1 = {
    "name" : "john",
    "notes" : [3,5,4]
    }
nums = d1["notes"]
if nums:
    avg = sum(d1["notes"])//len(d1["notes"])
    d1["notes"] = avg
else:
    d1["notes"] = 0

print(d1)

#sep alpha and digits in a words
n = input("enter the words:").split()
dic={}
for i in n:
    alpha=""
    digit=""
    for j in i:
        if j.isalpha():
            alpha+=j
        elif j.isdigit():
            digit+=j
    dic[alpha] = digit
print(dic)


