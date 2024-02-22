student_name=input("\nEnter Name:")
course_name=input("\nEnter Course Name:")

class_attended=int(input("\nEnter Classes Attended:"))
TOTAL_NUMBER_OF_CLASSES=15

percentage_attendance=(class_attended/TOTAL_NUMBER_OF_CLASSES ) * 100

if percentage_attendance >= 75:
    print("\nALLOWED")

else:
     medical_cause=input("\nDo you have medical problem?Y/N:")
     if medical_cause=="Y":
          print("\nALLOWED")
     else:
          print("\nNOT ALLOWED")
      
              

     





    

    



