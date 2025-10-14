try:
    a = int(input("a:"))
    b = int(input("b:"))
    print(a/b)
    print(num)

except ValueError:
    print("Invalid num")
except ZeroDivisionError:
    print("Num not valid by zero")
except:
    print("Error occurred")
finally:
    print("Executed successfully")

try:
    list1 = [12,45,23,5]
    print(list1[8])
except IndexError:
    print("index out of range")
finally:
    print("program ended")

#reverse a num using recursion
# def reverse(n,rem=0):
#     if n==0:
#         return rem
#     return reverse(n//10,rem*10+n%10)

# n= 12
# print(reverse(n))