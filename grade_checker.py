def grade_check():
    score = float(input("Enter Your Numbers:"))
    if score >= 90:
        grade ='A'
    elif score >= 80:
        grade ='B'
    elif score >= 70:
        grade ='C'
    elif score >= 60:
        grade ='D'
    else :
        grade='F'
    print(f"Your Grade is : {grade}") 
grade_check()
