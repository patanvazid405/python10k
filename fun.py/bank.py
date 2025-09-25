# 1.balance
# 2.credit
# 3.debit/withdrawal
# 4.pin Generator

pin = 1812
bal = 567

#print bal
def balance():
    return bal

#credit
def credit(n):
    global bal
    bal+=n
    return bal

#withdrawal
def draw(n):
    if n>bal:
        print("Not enough Money")
    return bal-n

print("enter a op \n1.bal \n2.credit \n3.withdrawal")
inp = input()

if inp==1:
    print(balance())
elif inp==2:
    print(credit(45222))
        
