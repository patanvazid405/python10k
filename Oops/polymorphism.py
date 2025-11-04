class shopping:
    def Add_to_cart(self,*args):

        if len(args)==1 and isinstance(args[0],str):
            print(f"{args[0]} is added to cart")

        elif len(args)==2 and isinstance(args[0],str) and isinstance(args[1],int):
            print(f"{args[0]} is added to cart with Quantity {args[1]}")
        
        elif len(args)==1 and isinstance(args[0],list):
            print(",".join(args[0]))
        else:
            print("Not Item Added in the cart")

customer1 = shopping()
customer1.Add_to_cart("Ac")
customer1.Add_to_cart("Mobile",3)
customer1.Add_to_cart(["laptop","washing machine"])


