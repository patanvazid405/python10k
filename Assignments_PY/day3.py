#day3
#1  find largest and smallest in the list
n = list(map(int,input().split()))
print(max(n))
print(min(n))

#2
#  Second Smallest Number (Without Using Built-in Methods) 


#3 Prime Numbers in a Given Range 
a,b = map(int,input().split())
for i in range(a,b+1):
    if i>1:
        is_prime  = True
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                is_prime = False
                break
        if is_prime:
                print(i,end=" ")