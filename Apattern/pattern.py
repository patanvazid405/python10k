n = 5

for row in range(1,n+1):
    for col  in range(1,row+1):
        print(col,end=" ")
    print()


for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


# pattern like
# 1
# 0 1
# 1 0 1
# 0 1 0 1
for row in range(1,n+1):
    if row%2 == 1:
        val =1
    else:
        val = 0
    
    for j in range(1,row+1):
        print(val,end=" ")
        val= 0 if val==1 else 1
    print()
        

#another logic
for row in range(1,n+1):
    for col in range(1,row+1):
        if ((row+col)%2==1):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

#       1
#     2 1 2
#   3 2 1 2 3
# 4 3 2 1 2 3 4

n = 4
for row in range(1,n+1):
    print(" "*(n-row),end="")
    for col in range(1,row+1):
        print(col,end=" ")
    print()


#triangular pyramid
rows = int(input("Enter rows: "))
for i in range(1,rows+1):
    res,rev="",""
    print(" "*(rows-i)*2, end="")
    for j in range(1,i+1):
        if j > 1:
            rev = str(j)+" "+rev
        res=res+str(j)+" "
    print(rev+res)


m = 4
val = 1
for i in range(1,m+1):
    for j in range(1,i+1):
        print(val,end=" ")
        val+=1
    print()

rows = int(input("Enter row: "))#4
val=1
for row in range(1,rows+1):
    for ele in range(1,row+1):
        print(val,end=' ')
        val+=1
    print()




