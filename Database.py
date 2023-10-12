student = {}       # student:grades
courseList = []    # List of courses

filename="data.txt"

def readData():
    try:
        fh=open(filename,"r")

    except FileNotFoundError:
        print("File not found")
        
    except Exception as err:
        print("Error {}".format(err))
    else:
        for line in fh:
            (stu,courses) = line.split("|")
            student[stu]={}    # Sets the value as an empty dictionary
            courses = courses.strip("\n")  #Removes the line feed
            courses = courses.strip(",")   #Removes the comma at the end of the line
            for coursepair in courses.split(","):
                (co,gr) = coursepair.split(":")
                student[stu][co] = gr
                if co not in courseList:   #Maintain a list of all courses
                    courseList.append(co)
        fh.close()
        
def writeData():
    try:
        fh=open(filename,"w")
    except Exception as err:
        print("Error {}".format(err))
    else:
        for (stu,course) in student.items():
            fh.write(stu+"|")
            for (co,gr) in course.items():
              fh.write(co+":"+str(gr)+",")
            fh.write("\n")
        fh.close()
        
def addStudent():
    studentName = input("What is the name of the student to add? ")
    if studentName not in student.keys():
        student[studentName] = {}
    else:
        print("{} is already in the database with {} courses".format(studentName,len(student[studentName])))

def deleteStudent():
    studentName = input("What is the name of the student to delete? ")
    if studentName in student.keys():
        del student[studentName]
    else:
        print("{} is not in the database".format(studentName))


def addCourse():
    studentName = input("What is the name of the student? ")
    if studentName in student:
        studentCourse = input("What is the course to add? ")
        if studentCourse not in courseList:
            courseList.append(studentCourse)
        studentGrade = input("What is the grade to add? ")
        student[studentName][studentCourse]=studentGrade
    else:
        print("Please add the student first!\n")
        addStudent()

def printReportCard():
    print("*** Report cards")
    for stu in student.keys():
        print("\n{}'s Report Card:".format(stu))
        for (co,gr) in student[stu].items():
            print("\t{:10}\t{}".format(co,gr))

def printClasses():
    print("**** Courses")
    courseList.sort()
    for co in courseList:
        print("\n{}:".format(co))
        for stu in student:
            if co in student[stu].keys():
                print("\t{:15}\t{}".format(stu,student[stu][co]))
            
            
def printMenu():
    print("\n1. Add a student")
    print("2. Add/update a course and grade")
    print("3. Print all report cards")
    print("4. Print classes and grades")
    print("5. Delete a student")
    print("6. Read data")
    print("7. Save data")
    print("8. Exit")

if __name__ == "__main__":
    
    choice = 0
    while choice != 8:
        printMenu()
        try:
            choice = int(input("Please select a menu item [1-7]: "))
        except Exception as err:
            print("Please select from the menu!")
        else:
            if choice == 1:
                addStudent()
            elif choice == 2:
                addCourse()
            elif choice == 3:
                printReportCard()
            elif choice == 4:
                printClasses()
            elif choice == 5:
                deleteStudent()
            elif choice == 6:
                readData()
            elif choice == 7:                
                writeData()
            elif choice == 8:
                break
            else:
                print("That isn't one of the choices. Please select from the menu!!")
    print("Thank you!")
    
