class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("Area:",self.length*self.width)
r=Rectangle(9,7)
r.area()
