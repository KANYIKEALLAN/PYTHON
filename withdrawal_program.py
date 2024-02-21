print("\n\t\t\t====menu====\t\t\t\n")
print("""
1.Deposit
2.Withdraw
3.Check balance            """)

code_number=int(input("\nEnter Option:"))
deposit_amount=0
withdraw_amount=0
current_balance=0
balance=0



if code_number==1:
    deposit_amount=int(input("\nEnter Deposit:"))
    if deposit_amount > 5000:
        current_balance=balance + deposit_amount
        print(f"\nCurrent Balance:{current_balance}\n")
    else:
        print("Transaction Failed")
    
elif code_number==2:
    balance=int(input("current balance:"))
    withdraw_amount=int(input("Enter Withdraw:"))
    if withdraw_amount < balance:
        current_balance=balance - withdraw_amount
        print(f"\ncurrent Balance{current_balance}\n")
    else:
        print("Transaction Failed")

elif code_number==3:
    balance=int(input("balance:"))
    print(f"\nCurrent Balance{balance}\n")
    
else:
    print("Invalid Option")
  


