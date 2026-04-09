class Employee:
    def details(self,name,salary):
        print(f"{name} : {salary}")
    
class Manager(Employee):
    pass

name=input("Enter employee name:")
salary=float(input("Enter salary:"))

E=Manager()
E.details(name,salary)
