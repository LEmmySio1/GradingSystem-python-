students = {} #Temporary Directory
    #add student
def add_student():
    name = input("Enter Student name: ")

    if name in students:
        print("Student is already registered")
        return
    #Precaution if the program falls through
    try:
        grade = float(input("Enter grade: "))

        if grade < 0 or grade > 100:
            print("Please enter a grade that is within the grading system")
            return
        
        students[name] = grade
        print("stduent grade added")

    except ValueError:
        print("Invalid input.Please enter a valid numebr")
    
    #view student list
def view_students():

    print("Function called")
    print("Student List")
    
    if not students:
        print("No Student Found")
        return 
    
    #\n lets you break inside of the same string
    print("\nstudents List")
    print("------------------")

    for name, grade in students.items():
        print(f"{name}: {grade}")
    
    #update grade list
def update_grade():
    name = input("Enter A Students Name: ")

    if name not in students:
        print("Student Not Found")
        return
    try:
    
        new_grade = float(input("Enter Updated Grade: "))

        students[name] = new_grade
        print("Grade Has Been Successfully Updated")

    except ValueError:
        print("An Invalid Input")
    #remove student from list
def remove_students():
    name = input("Enter student name: ")

    if name in students:
        del students[name]
        print("Student removed successfully")
    else:
        print("Student Not Found")
    #student statistics
def show_statistics():
    if not students:
        print("Student Not Found")
        return
    
    grades = list(students.values())

    average = sum(grades) / len(grades)
    highest_student = max(students, key=students.get)
    lowest_student = min(students, key=students.get)

    print("\nStatistics")
    print("------------------")
    print(f"Number of students: {len(students)}")
    print(f"Average grade: {average:.2f}")
    print(f"Highest grade: {highest_student} ({students[highest_student]})")
    print(f"Lowest grade: {lowest_student} ({students[lowest_student]})")

while True:
    print("\n===== STUDENT GRADE SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Grade")
    print("4. Remove Student")
    print("5. Statistics")
    print("6. Exit")    

    choice = input("Choose an Option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_grade()
    elif choice == "4":
        remove_students()
    elif choice == "5":
        show_statistics()
    elif choice == "6":
        print("Exit")
        break


