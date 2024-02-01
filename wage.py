worker_name=input("\nEnter Name:")
task_name=input("\nEnter Task:")
hours_worked=int(input("\nHours Worked:"))
RATE=30000


wage=hours_worked * RATE
allaowance=int(0.05 * wage)
gross_wage=allaowance + wage
tax=int(0.05 * gross_wage)
net_wage=gross_wage - tax

print(f"\nWage:{wage}\n\nAllowance:{allaowance}\n\nGross Wage:{wage}\n\nTax:{tax}\n\nNet Wage:{net_wage}\n\n")



