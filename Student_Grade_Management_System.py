def addStudent():
    name = int(input("Enter the Student name: "))
    marks = []
    
    print("Enter the marks in PCM: ")
    for i in range(3):
        m = int(input())
        marks.append(m)

    student = {"Name":name, "Physics":marks[0], "Chemistry":marks[1], "Mathematics":marks[2]}

    student_register.append(student)

    print("Student details added to the Register successfully")    
