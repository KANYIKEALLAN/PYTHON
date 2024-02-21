name=input("\nEnter Name:")
member=input("\nEnter Member Type:")
days_spent=int(input("\nEnter Days Spent:"))

rate=0

if days_spent < 5:
    if member=="Platinum":
        rate=2000
    elif member=="Gold":
        rate=1000
    else:
        print("\nInvalid")   

elif days_spent >=5 and days_spent <=10:
    if member=="Platinum":
        rate=2500
    elif member=="Gold" :   
        rate=3000
    else:
        print("\nInvalid")
elif days_spent > 10:
    if member=="Platinum":
        rate=3500
    elif member=="Gold":
        rate=5000
    else:
        print("\ninvalid")   
else:
    print("Invalid")    

amount=days_spent * rate

print(f"\nAmount:{amount}\n")   