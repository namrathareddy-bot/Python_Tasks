class Staff:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Proffessor(Staff):
    def display(self):
        print("Proffessor:",self.name,self.id)
class LabAssistant(Staff):
    def display(self):
        print("LabAssistance:",self.name,self.id)
class Administrator(Staff):
    def display(self):
        print("Administrator:",self.name,self.id)
p=Proffessor("Padma",1)
l=LabAssistant("Srinivas",2)
a=Administrator("Karthik",3)
p.display()
l.display()
a.display()
