count=1
students=5

while count <=students:
    student_name=input("\nEnter Name:")
    subject_1=float(input("\nEnter Math:"))
    subject_2=float(input("\nEnter Programming:"))
    subject_3=float(input("\nEnter Maintanance:"))

    total=int(subject_1 + subject_2 + subject_3)
    average=float(total/3)

    print(f"\n{student_name} your TOTAL is {total} and AVERAGE {average}\n")


    count+=1