list1 = ["vazid","Rajesh","niteesh"]
list2 = [89,78,56]
list3 = ["Nellore","Gudur","kavali"]

zipped_list = zip(list1,list2,list3)
print(list(zipped_list))

for name,num,place in zipped_list:
    print(f"{name} marks are {num} from {place}")


#unzip 

words = [('H',1),("E",2),('L',3),('L',4)]\

strr,intt = zip(*words)
print("".join(strr))
print(list(intt))