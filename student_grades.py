def student_grades_manager():
    student_grades={"deepak" : "A",
                    "Amit" : "B"
                    }
    print("1. Add new student")
    print("2. Update student Grades")
    print("3. Print all student details")
    
    choice =input("Enter 1, 2 or 3")
    if choice == "1":
        name = input("Enter Student Name: ")
        grade = input("Enter grades: ")
        student_grades[name]=grade
        print(f"Student {name} add with grade {grade}")
    elif choice == "2":
        name = input("Enter student name to update :")
        if name in student_grades:
            new_grade = input("Enter new grade :")
            student_grade[name] = new_grade
            print(f"{name}'s grade  Update to {new_grade}")
        else:
            print("Student not found :")
        
    elif choice == "3":
        print("All Student Details")
        print(student_grades)
    else:
        print("invalid choice")

student_grades_manager()





