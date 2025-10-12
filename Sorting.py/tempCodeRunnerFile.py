def selectionSort(n):
    for i in range(0,len(n)-1):
        for j in range(i+1,len(n)):
            if n[j]<n[i]:
                n[i],n[j]= n[j],n[i]


n = [12,45,-1,56,5]
selectionSort(n)
print(n)