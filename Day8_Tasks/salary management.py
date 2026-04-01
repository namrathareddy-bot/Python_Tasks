#Employee salary management system
'''
A company stores employee data in a file employees.txt in the format:
EmployeeName Salary
Write a Python program that:
● Reads employee data from the file
● Displays all employee details
● Finds the employee with the highest salary
● Appends a new employee record to the file

'''

import os

def salary_management_system():
    try:
        # Step 1: Create file if not exists
        if not os.path.exists("employees.txt"):
            print("File not found!!")
            choice = input("Enter choice to create a file: [y/n] ")

            if choice.lower() == 'y':
                with open("employees.txt", 'w') as employees_details:
                    n = int(input("Enter number of employees: "))
                    
                    for i in range(1, n + 1):
                        details = input("Enter name and salary (e.g. Rahul 25000): ")
                        employees_details.write(details + "\n")   

                print("Details entered successfully\n")

            else:
                print("Okay. Exiting...")
                return

        # Step 2: MENU LOOP (runs always)
        while True:
            print("\n------ MENU ------")
            print("1. Read file")
            print("2. Display records")
            print("3. Find highest salary")
            print("4. Append new employee")
            print("5. Exit")

            option = int(input("Enter option: "))

            # 1. Read file
            if option == 1:
                with open("employees.txt", 'r') as emp_details:
                    data = emp_details.read()
                    print("File read successfully\n")
                    print(data)

            # 2. Display records (same as read but kept separate as per question)
            elif option == 2:
                with open("employees.txt", 'r') as file:
                    content = file.read()
                    print("Below is the content:\n")
                    print(content)

            # 3. Highest salary
            elif option == 3:
                highest = 0
                emp_name = ""

                with open("employees.txt", 'r') as file:
                    for line in file:
                        data = line.split()
                        if len(data) == 2:
                            name = data[0]
                            salary = int(data[1])

                            if salary > highest:
                                highest = salary
                                emp_name = name

                if emp_name:
                    print("Highest salary employee:", emp_name)
                    print("Salary:", highest)
                else:
                    print("No data found")

            # 4. Append new employee
            elif option == 4:
                new_employee = input("Enter new employee name and salary: ")
                with open("employees.txt", 'a') as f:
                    f.write(new_employee + "\n")   
                print("Employee added successfully")

            # 5. Exit
            elif option == 5:
                print("Exiting...")
                break

            else:
                print("Invalid option! Try again.")

    except (ValueError, FileNotFoundError):
        print("Error: Invalid input or file issue")

salary_management_system()
                
            
                
