employee_name=input("\nEnter Name:")
hours_worked=int(input("\nHours Worked:"))
RATE=30000

wage=int(hours_worked * RATE)


if wage>=500000:
    tax=0.1 * wage

else:
    tax=0

net_wage=wage - tax

print(f"\nDear {employee_name} your pay for {hours_worked}hrs is {net_wage}\n")
