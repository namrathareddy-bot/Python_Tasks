# Q1: Develop a Python program to manage student marks for three subjects.Store the subject names in a tuple, maintain unique student names in a set, and store each student’s marks in a list inside a dictionary where the key is the student name. Create user-defined functions to add a student with marks, display all student records, and calculate the average marks of a student. Implement a recursive function to calculate the total marks from the list of marks. The program should interact with the user through a simple menu. Also include exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError (average calculation issues), TypeError (incorrect data type in marks), and NameError (when a student name entered does not exist in the dictionary).

def sum_marks(marks):
    if not marks:
        return 0
    return marks[0]+sum_marks(marks[1:])

def std_details():

    subjects=("Math", "Science", "English")
    student_names=set()
    std_marks={}

    while True:
        print("\n1. Add Student\n2. Display Students\n3. Calculate Average\n4. Exit")
        choice=input("Enter choice: ")

        try:
            if choice=='1':
                name=str(input("Enter student name: "))
                marks=[]
                for sub in subjects:
                    marks.append(float(input(f"Enter marks for {sub}: ")))
                std_marks[name]=marks
                student_names.add(name)

            elif choice=='2':
                for name, m in std_marks.items():
                    print(f"{name}: {m}")

            elif choice=='3':
                name=input("Enter student name: ")
                if name not in std_marks:
                    raise NameError("Student not found!")

                total=sum_marks(std_marks[name])
                avg=total / len(std_marks[name])
                print(f"Total: {total}, Average: {avg}")

            elif choice=='4':
                break

            else:
                print("Enter choice numbers only")

        except ValueError:
            print("Error: Please enter Characters only.")
        except ValueError:
            print("Error: Please enter numbers only.")
        except NameError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: No marks found to calculate average.")
        except TypeError:
            print("Error: Incorrect data type encountered.")

std_details()
