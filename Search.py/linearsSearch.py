#linear
def linear(num,el):
    for i in range(0,len(num)):
        if num[i]==el:
            return i
    return -1
num =[12,45,2,67,89]
el = 2
res = print(linear(num,el))
if res != -1:
    print(f"{el} at {res}")

#binary search
def binarysearch(n,el):
    n.sort()
    global steps
    low = 0
    high = len(n)-1
    while low<=high:
        mid = (low+high)//2
        steps+=1
        if n[mid]==el:
            return "found"
        elif n[mid]<el:
            low=mid+1
        elif n[mid]>el:
            high=mid-1
    return -1

n =[3,5,8,12,45]
el =5
steps = 0
print(binarysearch(n,el))
print(steps)

