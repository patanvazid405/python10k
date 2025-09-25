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