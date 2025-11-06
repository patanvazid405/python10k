#Dunder Methods like +,-,<,>,==,str,*,/
#we use them by preBuilt-methods -> __add__ __sub__ __mul__ __str__ __gt__ __gl__ __eq__ __len__
class Product:
    def __init__(self,name,price,warranty=None):
        self.name = name
        self.price = price
        self.warranty = warranty
    
    #using of str and to print the data
    # def __str__(self): 
    #     return f"Product: {self.name} \nPrice: {self.price} \nWarranty: {self.warranty}" 
    
    def __str__(self):
        return str(self.price)

    #using add __add__
    def __add__(self,other):
        return Product("combo price",self.price+other.price)
    
    #using  sub __sub__
    def __sub__(self,other):
        return Product("sub price",self.price-other.price)
    
    #using GT __gt__
    def __gt__(self,other):
        if self.warranty > other.warranty:
            return f"{self.name} having more warranty"
        return f"{other.name} having more warranty"

p1 = Product("Laptop",50000,2)
p2 = Product("AC",60000,4)
p3 = Product("TV",30000,3)

print(p1+p2+p3) #adding price of three items/products

print(p1-p2+p3)

print (p1>p2)
# print(p1)
# print(p2)
    
#other example
class Bike:
    def __init__(self,name,mileage):
        self.name = name
        self.mileage = mileage
    
    def __repr__(self):
        return f"Bike Name: {self.name} Mileage: {self.mileage}"

b1 = Bike("hero",55)
print(b1)



# Practice work

# Take class called Book with data (author name, price)
# Implement add, sub, gt magic methods to compare prices of book objects

class Book:
    def __init__(self,author_name,price):
        self.author_name = author_name
        self.price = price
        
    def __add__(self,other):
        return Book("price",self.price+other.price)
        
    def __sub__(self,other):
        return Book("Price",self.price-other.price)
    
    def __gt__(self,other):
        if self.price > other.price:
            return f"{self.author_name} is more price {self.price}"
        else:
            return f"{other.author_name} is more price {self.price}"
    
    def __str__(self):
        return str(self.price)
        
    
    
b1 = Book("vazid",200)
b2 = Book("patan",300)
b3 = Book("Dhoni",400)

print(b1-b2+b3)
print(b1>b2>b3)

