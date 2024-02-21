employee_name=input("\nEnter Name:")
principal_amount=int(input("\nEnter Amount:"))
time=int(input("\nEnter Time in Days:"))

rate=0


if principal_amount>10000000:
    rate=0.05 
elif principal_amount>=5000000 and principal_amount<=10000000:
    rate=0.1 
elif principal_amount<5000000 and principal_amount>= 0:
    rate=0.15 

else:
    print("\nInvalid")

simple_interest=int(principal_amount * time * rate)

print(f"\nSimple Interest:{simple_interest}\n")

