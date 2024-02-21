student_name=input("\nEnter Student Name:")
registration_number=input("\nEnter Student Regn Number:")

subject_score1=float(input("\nEnter Math:"))
subject_score2=float(input("\nEnter Programming:"))
subject_score3=float(input("\nEnter Islam:"))
subject_score4=float(input("\nEnter Computer Maintainance:"))


total_score=float(subject_score1 + subject_score2 + subject_score3 + subject_score4)
average=float(total_score / 4)


print(f"\nTotal Score:{total_score}\n\nAverage Score:{average}\n\t\t\n\n***Thanks***\t\t\n\n")
