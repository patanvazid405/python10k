set1 = {12,35,24,25}
set2 = {2,35,4,45}

#add adds one el to the set
set2.add(23)
print(set2)

#update -> adds multiple el like adding into the set
set1.update({67,89,12})
print(set1)

#pop removes an el randomly from the set
set3 = {"vazid",22,"MGR",86}
print(set3.pop())
print(set3)

#remove ->removes an random el the set
set3.remove(22)
print(set3)

#clear -> makes an empty set 
set4 = {46,74,6,576}
set5 = set4.copy()
set4.clear()
print(set4)
print(set5)

#union -> like merging two sets 
set1 = {1,2,3,5,6}
set2 = {5,6,7,8}
new = set1.union(set2)
print(new)

#intersection  ->common in both sets
sett = set1.intersection(set2)
print(sett)

#difference -> like different in set1 or set2
diff = set1.difference(set2)
diff2 = set2.difference(set1)
diff3 = set2.symmetric_difference(set1)
print(diff)
print(diff2)
print(diff3)

#perfect num 
num = 6
summ =0
sq = num**2
for i in range(1,num//2+1):
    if num%i==0:
        summ+=i
print(summ) 

#automorphic 
num = 74
length = len(str(num))
sq = num**2
last = sq%10**length
print(last)
print(num)
print(sq)


#replace elements in list by its rank
# 23 56 1 7 8 -> original list
# 4  5  1 2 3 -> rank 

list1 = [int(i) for i in input().split()]
print(list1)

numSort = sorted(list1)

for i in list1:
    for j in range(0,len(numSort)):
        if numSort[j] == i:
            print(j+1,end=" ")

    








