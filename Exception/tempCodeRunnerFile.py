def withdraw(bal,amount):
    if amount>0:
        if bal<amount:
            print(f"Amount: {amount-bal} Withdrawal Successfully")
    else:
        raise ValueError("Insufficient Balance")

try:
    withdraw(1200,500)
except ValueError as msg:
    print(msg)