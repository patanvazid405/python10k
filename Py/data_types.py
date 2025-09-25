#Integer
distance = 507
distance_km = int(input("Enter the Distance in KM :"))
print(f"Total distance is {distance} and type is {type(distance)}")
print(f"Total distance is {distance_km} and type is {type(distance_km)}")

#float
Temperature = 37.5
TempNow = float(input("Enter the Celcius:"))
print(f"Temerature is {Temperature} and type is {type(Temperature)}")
print(f"Total distance is {TempNow} and type is {type(TempNow)}")

#complex
complexNum = 1+3j
compNum2 = complex(input("Enter a Complex Number:"))
print(f"Complex Number is {complexNum} and type is {type(complexNum)}")
print(f"Complex Number is {compNum2} and type is {type(compNum2)}")

#boolean
Rain = True
Sunny = bool(input("How's it Outside:"))
print(f"Is it Raining = {Rain} and type is {type(Rain)}")
print(f"Outside Today {Sunny} and type is {type(Sunny)}")

#Dictionary
student_details ={
        "name": "vazid",
        "age" : 22,
        "clg" : "MGR",
        "Marks":
        {
            "C++" : 80,
            "Python" : 90,
            "Networks" : 85,
        }
}
print(f"Student Details {student_details} and type is {type(student_details)}")
print(student_details["age"])
print(student_details["Marks"]["C++"])

#sets
sectionA = {"rajesh","niteesh","sampath"}
sectionB = set(input("Enter Names:").split(" "))
print(f"Section A {sectionA} and type is {type(sectionA)}")
print(f"Section B {sectionB} and type is {type(sectionB)}")
print(sectionA.intersection(sectionB))

#tuples
user_details = ("vazid",22,"kphb","airtel")
user_info = tuple(input("Enter the Details:").split(" "))
print(f"User details {user_details} and type is {type(user_details)}")
print(f"User info {user_info} and type is {type(user_info)}")

#lists
Emp1 = [101,"vazid",22,"Mudivarthi Palem"]
Emp2 = list(input("Enter Emp Details:").split(" "))
print(f"Employee details {Emp1} and type is {type(Emp1)}")
print(f"Employee info {Emp2} and type is {type(Emp2)}")

#string
Msg1 = "hello world"
Msg2 = str(input("Enter A Word Here:"))
print(f"Message is {Msg1} and type is {type(Msg1)}")
print(f"Message is {Msg2} and type is {type(Msg2)}")


inp = int(input("Num:"))
sum =0
j = 0
while j<=inp:
    sum+=j
print(sum) 


a = 5 
b = 4
print(a&b)
print(a|b)
print(a^b)
print(~(23234832))
print(a<<b)
print(a>>b)
