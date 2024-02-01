student_name=input("Enter Name:")
course_work_mark=int(input("Enter Course Work Marks:"))
exam_score=int(input("Enter Exam Score:"))

score_out_70=(exam_score/100)*70
Final_score=int(score_out_70) + course_work_mark

print(f"Exam/70: {score_out_70} \nFinal Score:{Final_score}")

