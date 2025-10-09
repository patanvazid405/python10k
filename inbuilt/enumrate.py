#to iterate using counter for list tuple string 
#1
list1 = ["vazid","patan","riyaz","rajiya"]
res = list(enumerate(list1,start=1))
print(res)
for i in res:
    print(f"{i[1]} is at position {i[0]}")
#2
word = "ojas gambheera"
fin = list(enumerate(word,start=0))
print(fin)

list2 = ["rajesh","niteesh","teja","karthik"]
rev = list(enumerate(list2,start=1))
print(rev)

for i in rev:
    print(f"{i[1]} at position {i[0]}")
    


