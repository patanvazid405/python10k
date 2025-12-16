# prime number
num = 12

if num > 1:
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            print("Not a prime number")
            break
        else:
            print("prime number")
else:
    print("enter a valid number")
