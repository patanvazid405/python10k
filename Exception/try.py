def eligible(percent):
    if percent>75:
        print("passed")
    else:
        raise ValueError("Not Eligible")

try:
    eligible(8)
except ValueError as msg:
    print(msg)

#assert for strong num
import math
num = int(input())
temp = num
res = 0
while temp!=0:
    rem = temp%10
    res += math.factorial(rem)
    temp = temp//10
assert num == res
print("Strong Num")

#using assert in
def validate(num):
    for i in num:
        assert (i<50),"failed"
        print("passed")
list1 = [12,45,35,76,98,24]

try:
    validate(list1)
except AssertionError as msg:
    print(msg)

