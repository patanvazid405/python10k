#linear
def linear(num,el):
    for i in range(0,len(num)):
        if num[i]==el:
            return "Found"
        else:
            return "Not found"
num =[12,45,67,89]
print(linear(num,2))

