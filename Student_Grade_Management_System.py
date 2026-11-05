def addStudent():
    name = input("Enter the Student name: ")
    marks = []
    
    print("Enter the marks in PCM: ")
    for i in range(3):
        m = int(input())
        marks.append(m)

    student = {"Name":name, "Physics":marks[0], "Chemistry":marks[1], "Mathematics":marks[2]}

    student_register.append(student)

    print("Student details added to the Register successfully") 

def viewStudentRecords():

    if len(student_records) == 0:
        print("Student Records is empty")
        return

    print("-----STUDENT RECORDS-----")
    print("NAME\tPHYSICS  MARKS\tCHEMISTRY MARKS\tMATHEMATICS MARKS")
    for student in student_records:
        print(f"{student['Name']}\t{student['Physics']}\t{student['Chemistry']}\t{student['Mathematics']}")

def calculateAverage():
    if len(student_records) == 0:
        print("No Student details found: ")
        return
    
    found = 0
    name = input("Enter the student name: ")


    
