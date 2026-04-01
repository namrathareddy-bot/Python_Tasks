#Student Marks File Analyzer
'''A teacher stores student marks in a file marks.txt in the format:
Name Marks

Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the class

'''

import os

def student_marks_analyzer():
    try:
        if not os.path.exists("marks.txt"):
            print("No file found")
            choice = input("Enter choice to create a file or not [y/n]: ")

            if choice.lower() == 'y':
                with open("marks.txt", 'w') as students:
                    n = int(input("Enter number of students: "))
                    
                    for i in range(1, n + 1):
                        stu = input("Enter name and marks (e.g. Rahul 80): ")
                        students.write(stu + "\n")

                print("Students added successfully\n")

            else:
                print("Okay! No file created.")
                return


        while True:
            print("\n------ MENU ------")
            print("1. Read file content & Display student records")
            print("2. Calculate average")
            print("3. Exit")

            option = int(input("Enter option: "))

            if option == 1:
                with open("marks.txt", 'r') as students:
                    content = students.read()
                    print("\nContent read successfully")
                    print(content)

            elif option == 2:
                total = 0
                count = 0

                with open("marks.txt", 'r') as file:
                    for line in file:
                        data = line.split()
                        if len(data) == 2:
                            marks = int(data[1])
                            total += marks
                            count += 1

                if count > 0:
                    avg = total / count
                    print("\nAverage Marks:", avg)
                else:
                    print("No data found")

            elif option == 3:
                print("Exiting program...")
                break   

            else:
                print("Invalid option! Try again.")

    except (TypeError, FileNotFoundError, ValueError):
        print("Error: Invalid input or file issue")

student_marks_analyzer()
