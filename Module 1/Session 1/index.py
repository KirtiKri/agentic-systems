bal= 10000
w_amount = int(input("Enter Withdrawal amount:"))
if w_amount <= bal:
    bal = bal - w_amount
    print("Withdrawal Sucessfull!!!")
    print(f"Remaining Amount= {bal}") 
else:
    print("Insufficient Amoount!!!")
