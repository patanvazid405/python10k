m = 4
val = 1
for i in range(1,m+1):
    for j in range(1,i+1):
        print(val,end="")
        val+=1
    print()

rows = int(input("Enter row: "))#4
val=1
for row in range(1,rows+1):
    for ele in range(1,row+1):
        print(val,end=' ')
        val+=1
    print()